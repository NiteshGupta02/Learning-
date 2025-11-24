#Language Translator Using GUI

from googletrans import Translator
from tkinter import *

def funcEnglish():
    s=t.translate(src.get(),"en")
    dest.set(s.text)
def funcHindi():
    s=t.translate(src.get(),"hi")
    dest.set(s.text)
def funcPunjabi():
    s=t.translate(src.get(),"pa")
    dest.set(s.text)
def funcFrench():
    s=t.translate(src.get(),"fr")
    dest.set(s.text)

root=Tk()
root.title("CETPA Language Translator")
root.geometry("500x500")
root["bg"]="orange"
lbl=Label(root,text="Enter Text in Any Language",font=20,width=35)
lbl.grid(row=0,column=0,columnspan=4)

src=StringVar()
entMsg=Entry(root,textvariable=src,font=1,width=35)
entMsg.grid(row=1,column=0,columnspan=4)

btnEnglish=Button(root,text="English",font=20,bg="yellow",width=8,command=funcEnglish)
btnEnglish.grid(row=2,column=0)
btnHindi=Button(root,text="Hindi",font=20,bg="yellow",width=8,command=funcHindi)
btnHindi.grid(row=2,column=1)
btnPunjabi=Button(root,text="Punjabi",font=20,bg="yellow",width=8,command=funcPunjabi)
btnPunjabi.grid(row=2,column=2)
btnFrench=Button(root,text="French",font=20,bg="yellow",width=8,command=funcFrench)
btnFrench.grid(row=2,column=3)

dest=StringVar()
entconvMsg=Entry(root,textvariable=dest,font=1,width=35)
entconvMsg.grid(row=4,column=0,columnspan=4)
t = Translator()

root.mainloop()
