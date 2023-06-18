import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import requests

  
# This module is imported so that we can 
# play the converted audio
import pygame
pygame.init()
model = whisper.load_model("base")

# deepL api request
url = "https://api-free.deepl.com/v2/translate"
api_key = '8edcabcf-2501-1d75-f520-82e2684e2611:fx'
headers = {"Content-Type": "application/x-www-form-urlencoded"}


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

def translate_text(input_text, source_lang, target_lang):
    payload = {
        "auth_key": api_key,
        "text": input_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["translations"][0]["text"]
    else:
        print("Translation failed. Status code:", response.status_code)
        return None

# The text that you want to convert to audio
def text_to_speech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    myobj.save("speech.mp3")
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# main method
def voice_transcription():
    audio_filename = create_audio_file()
    transcription_response = send_audio_to_whisper(audio_filename)
    translated_text = translate_text(transcription_response, "EN", "JA")
    print(translated_text)
    if translated_text is not None:
        text_to_speech(translated_text, 'ja')
        
    

voice_transcription()
