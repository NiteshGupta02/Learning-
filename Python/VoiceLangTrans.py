import speech_recognition as sr
from googletrans import Translator
import gtts
import pyttsx3
engine=pyttsx3.Engine()

# def takeCommand():  # it takes microphone input from the user and return the string output
# from tkinter import *
# root=Tk()
r = sr.Recognizer()  # recogniser class helps in recognising the audio
with sr.Microphone() as source: #source is an object of Microphone() class
        print("Listening...")
        r.pause_threshold = 0.5  # it refers to the amount of time gap after which the audio is supposed to be complete
        r.energy_threshold = 300
        audio = r.listen(source)  # digitaldata of whatsoever hs been spoken will be stored in audio
        print(audio)
        print("Recognising...")
        query = r.recognize_google(audio, language="hi")
        print("Hindi Message:", query)
t=Translator()
res=t.translate(query,"en")
print("English Message:", res.text)
engine.say(res.text)
engine.runAndWait()
