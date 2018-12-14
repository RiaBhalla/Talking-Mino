from gtts import gTTS 
import playsound
import os
from tempfile import TemporaryFile
while True:
  gTTS(text='text to be converted', lang='en') 
  tts.save("your_file.mp3")
  playsound.playsound("C:/Users/Desktop/yourfile.mp3",True)
