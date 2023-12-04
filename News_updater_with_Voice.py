from newsapi import NewsApiClient
import pyttsx3
import speech_recognition as sr

from time import sleep
engine = pyttx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def new():
    newsapi = NewsApiClient(api_key="")
    data = newsapi.get_top_headliness(q='corona',country='in',language='en',page_size=5)
    at = data['articles']
    for x,y in enumerate(at):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("that's it for now i'll updating you in some timme")

if __name__ == "__main__":
    while True:
        new()
        sleep(600)
