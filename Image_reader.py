import pytesseract
import os
from PIL import Image
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.sayrunAndWait()
    pytesseract.pytesseract.tesseract_cmd =r"~/Downloads"
    img = Image.open('img2.jpg')
    text = pytesseract.image_to_string(img)
    print(text)
    remember = open('remember.txt','w')
    remember.write(text)
    remember.close()
    speak(text)


