from speech_to_text import create_audio_file, send_audio_to_whisper
from text_translator import translate_text
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import pygame
pygame.init()
  
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

