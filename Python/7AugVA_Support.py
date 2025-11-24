""""""
"""
Pawan is asking:
Due to AI, IT sector is seeing a downfall.
Completely incorrect

Last Big recession in IT Sector was in 2008 and now in 2023. 
Reason is the US economy.  

AI can replace you in future if you don't learn AI

Project in Python: Virtual Assistant
"""


"""
import datetime   #To access current date and time
import speech_recognition as sr  #Speech to Text Conversion
import pyttsx3     #Python Text to Speech, version x3
import wikipedia    #to access wikipedia content
import webbrowser   #to access web browser
import os           #Operating System related library


import speech_recognition as sr  #To install this library then 
                                #search SpeechRecognition

"""
# import pyttsx3
# engine=pyttsx3.init()     #pyttsx3.Engine()
# print(type(engine))
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate', 150)
# engine.say("Hello How Are You, how may I help you today")
# engine.runAndWait()

# #New Program
# import datetime
# t=datetime.datetime.now()
# hour=t.hour
# print(hour)
# min=t.minute
# print(min)
# print(t)
#
# def wishMe():
#     hour=int(datetime.datetime.now().hour)
#     # minute= int(datetime.date
#     time.now().minute)
#     if (hour>=0 and hour<12):
#         speak("Good Morning Boss!")     #Text to Speech
#     elif(hour>=12 and hour<18):
#         speak("Good Afternoon Boss")
#     else:
#         speak("Good Evening Boss")
#     speak("I am your Virtual Assistant, How may I help you?")


# #New Program
#
# import speech_recognition as sr
# from googletrans import Translator
# import pyttsx3
# engine=pyttsx3.Engine()
#
# def speak(text): #to speak. Text to Speech
#     engine.say(text)
#     engine.runAndWait()
# # def takeCommand():  # it takes microphone input from the user and return the string output
# # from tkinter import *
# # root=Tk()
# r = sr.Recognizer()  # recogniser class helps in recognising the audio
# with sr.Microphone() as source: #source is an object of Microphone() class
#         print("Listening...")
#         r.pause_threshold = 0.5  # it refers to the amount of time gap after which the audio is supposed to be complete
#         r.energy_threshold = 300
#         audio = r.listen(source)  # digitaldata of whatsoever hs been spoken will be stored in audio
#         print(audio)
#         print("Recognising...")
#         query = r.recognize_google(audio, language="hi")
#         print("Hindi Message:", query)
# t=Translator()
# res=t.translate(query,"en")
# print("English Message:", res.text)
# speak(res.text)







# engine.say("res.text")
# engine.runAndWait()
#root.mainloop()
        # engine.runAndWait()
    # try:
    #     print("Recognising...")
    #     query = r.recognize_google(audio, language="en-in")
    #     print("User Said:", query)
    # except Exception as e:
    #     print("Say that again please!")
    #     return "None"
    # return query



# #New Program
# f=open("D://vikas/cetpa3.txt","r")
# print(f.read())
# f.close()

# #New Program
# with list() as L:
#     print(L)

# #New Program
# with open("D://vikas/cetpa3.txt","r") as f:
#     # f=open("D://vikas/cetpa3.txt","r")
#     print(f.read(5))
# f.read(10)

# #New Program
# import random
# L1=[2,3,4,7,8]
# ch=random.choice(L1)
# print(ch)

# #New Program
# from googletrans import Translator
# t = Translator()
# res = t.translate("How are you","hi")
# print(res.text)


# # New Program
# def speak(text): #to speak. Text to Speech
#     engine.say(text)
#     engine.runAndWait()
# import pyttsx4
# engine=pyttsx4.init()
# sp = "Hello How Are You, how may I help you today"
# # speak(sp)
#
# engine.say(sp)
# engine.runAndWait()


