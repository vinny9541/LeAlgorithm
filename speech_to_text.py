import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os

#openai.api_key = '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'

model = whisper.load_model("base")


def create_audio_file():
    # Choose your desired sample rate
    sample_rate = 44100

    # Choose duration in seconds
    duration = 5

    print("Recording...")

    # Record audio for the specified duration at the specified sample rate
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)

    # Wait for the recording to finish
    sd.wait()

    print("Recording complete. Saving to file.")

    # Save the recording to a WAV file
    filename = 'output.wav'
    write(filename, sample_rate, recording)

    return filename

def send_audio_to_whisper(filename):

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(filename)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    return result.text
    

def main():
    audio_filename = create_audio_file()
    transcription_response = send_audio_to_whisper(audio_filename)
    
    print(transcription_response)
    print("Deleting audio file.")
    os.remove(audio_filename)

main()
