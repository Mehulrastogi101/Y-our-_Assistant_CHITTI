import speech_recognition as sr
import webbrowser as wb
from win32com.client import Dispatch
import os


r1 = sr.Recognizer()
r2 = sr.Recognizer()

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

def Openfolder():
    path = 'C:\\Users\\manu\\Desktop'
    open(path, "r") #Permission Denied


def youtube():
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        speak('Welcome to youtube ')
        print('Welcome on youtube ')
        speak('say your query')
        print('say your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url + get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

def google():
    url = 'https://www.google.com/search?client=firefox-b-d&q='
    with sr.Microphone() as source:
        speak('Welcome to google ')
        print('Welcome on google ')
        speak('say your query')
        print('say your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url + get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

with sr.Microphone() as source:
    speak('Hi Manohar')
    print('Hi Manohar')
    speak("speak Youtube if you want to search something from youtube")
    print("speak Hello if you want to search something from youtube")
    audio = r1.listen(source)
    text = r1.recognize_google(audio)
    print(text)

if 'YouTube' in text:
    speak('Hello')
    print('Hello')
    youtube()
elif 'Google' in text:
    speak('Hello')
    print('Hello')
    google()

else:
    print('Bye')
