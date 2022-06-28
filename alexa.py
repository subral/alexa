import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from flask import Flask
lis = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

engine.say("hey i'm alexa how can i help you")
engine.runAndWait()


def take():
    try:
        with sr.Microphone() as sourse:
            print("listining...")
            vo = lis.listen(sourse)
            cam = lis.recognize_google(vo)
            cam = cam.lower()

    except:
        pass
    return cam


def talk():

    cammand = take()
    if "play" in cammand:
        song=cammand.replace("play", "")
        engine.say("playing"  + song )
        pywhatkit.playonyt(song)
        engine.runAndWait()

    elif "google" in cammand:
            a = "who is google you fucking piece of shit"
            print(a)
            engine.say(a)
            engine.runAndWait()

    elif "siri" in cammand:
            b = "who is siri you worthless shit"
            engine.say(b)
            print(b)
            engine.runAndWait()

    elif "search" in cammand:
        yo = cammand.replace("search","")
        engine.say("ready to go" + yo)
        pywhatkit.search(yo)
        engine.runAndWait()

    elif "time" in cammand:
        to = cammand.replace("time","")
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        engine.say(time)
        engine.runAndWait()

    elif "who is" in cammand:
        tp = cammand.replace("who is","")
        s = wikipedia.summary(tp)
        print(s)
        engine.say(s)
        engine.runAndWait()

    elif "i love you" in cammand:
        f = "I already have relationship with my charger"
        engine.say(f)
        engine.runAndWait()

    else:
        engine.say("say something")
        engine.runAndWait()


while True:
    talk()
