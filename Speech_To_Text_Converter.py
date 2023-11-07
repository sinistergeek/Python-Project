import speech_recognition
def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        print("I am trying to hear you: ")
        audio=microphone.listen(live_phone)
        try:
            phrase=microphone.recognize_google(audio,language='en')
            return phase

        except speech_recognition.UnkownValueError:
            return "I didn't understant what you said"

if __name__ == '__main__':
    pharse = record_voice()
    with open('you_said_this.txt','w') as file:
        file.write(phrase)
    print('the last sentence you spoke was saved in you_said_this.txt')
