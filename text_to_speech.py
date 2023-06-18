from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'こんにちは、お元気ですか?'
  
# Language in which you want to convert
language = 'ja'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("speech.mp3")
  
# Playing the converted file
os.system("speech.mp3")