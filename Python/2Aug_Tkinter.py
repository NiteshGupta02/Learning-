""
"""
Starting tkinter today
GUI Programming

Till now we have developed Console Based Applications:


GUI: Graphical User Interface: tkinter
tkinter is a python framework (library/package) used to develop GUI windows applications
"""
# #New Program
# import tkinter as tk
# root=tk.Tk()        #root is an object of Tk Class, to create root window
# root.geometry("300x500")
# root.mainloop()     #Infinte Loop

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500+100+200")
# root.mainloop()

"""
Button Widget: Button Class: Create object of the class and then define the geometry
                of the Button widget

Layout/Geometry of Widget: 
3 Options:
1. pack Geometry:
widget.pack(side='exact_side)'
default side is top
2. place Geometry:
widget.place(x=pixels,y=pixels)
3. grid Geometry:
widget.grid(row=row_no, column=column_no

"""

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# btn=Button(root,text="Submit")
# btn.pack(side="left")
# root.mainloop()


# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,text="Submit",bg="Yellow",fg="red",width=20,height=3,font=100)
# btn.pack(side="bottom")
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="CETPA",width=20,height=4,bg="Blue",fg="White",font=20)
# btn.place(x=50,y=100)
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# btn1=Button(root,text="CETPA",width=20,height=4,bg="Blue",fg="White",font=20)
# btn1.grid(row=0,column=0)
# btn2=Button(root,text="HELLO",width=10,height=4,bg="Blue",fg="White",font=20)
# btn2.grid(row=1,column=1)
# btn3=Button(root,text="WELCOME",width=20,height=4,bg="Blue",fg="White",font=20)
# btn3.grid(row=2,column=0)
# root.mainloop()


# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# btn1=Button(root,text="CETPA",width=20,height=4,bg="Blue",fg="White",font=20)
# btn1.grid(row=0,column=0)
# btn2=Button(root,text="HELLO",width=10,height=4,bg="Blue",fg="White",font=20)
# btn2.grid(row=0,column=0)
# btn3=Button(root,text="WELCOME",width=20,height=4,bg="Blue",fg="White",font=20)
# btn3.grid(row=2,column=0)
# root.mainloop()


# #New Program
# from tkinter import *
# root1=Tk()
# root1.title("First Window")
# root1.geometry("400x400")
# root2=Tk()
# root2.title("Second Window")
# root2.geometry("400x400")
# btn=Button(root1,text="Welcome",font=20)
# btn.grid(row=0,column=0)
#
# root1.mainloop()

"""
Event: Any action performed is an event.
Event_Handler: A function which is called after the event is fired.
"""
# #New Program
# from tkinter import *
# def handler():
#     print("Button is Clicked")
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,text="CETPA",font=20,command=handler)
# btn.pack()
# root.mainloop()

# #New Program
# from tkinter import *
# def handler():      #Left Click Event Handler
#     print("Button is Clicked")
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,text="CETPA",font=20,command=handler)
# btn.pack()
# root.mainloop()

"""Button Widget: For Button. Button is designed to take mouse events from user
Label Widget: To display data on screen
"""

#New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# lbl=Label(root,text="First Button",font=20,fg="green")
# lbl.grid(row=0,column=0)
# btn=Button(root,text="Submit",font=20)
# btn.grid(row=0,column=1)
# root.mainloop()

"Entry Widget: is Single Line Text Input Widget"

# #New Program
# from tkinter import *
# def handler():
#     s=name.get()
#     print(s)
# root=Tk()
# root.geometry("500x500")
# lbl=Label(root,text="Enter Your Name:  ",font=20,fg="green")
# lbl.grid(row=0,column=0)
# name=StringVar()            #IntVar()
# entr=Entry(root,font=20,textvariable=name)
# entr.grid(row=0,column=1)
# btn=Button(root,text="Submit",font=20,command=handler)
# btn.grid(row=1,column=1)
# root.mainloop()


"""There is No Negative Marking in our Class"""


# #New Program
# from tkinter import *
# def submit_Data():
#     print("Cust ID:",var_id.get())
#     print("Cust Name:", var_name.get())
#     print("Cust Age:", var_age.get())
#
# root=Tk()
# root.geometry("500x500")
# lbl_id=Label(root,text="Enter Your Id:",font=20,bg="Yellow",width=20)
# lbl_id.grid(row=0,column=0)
# var_id=StringVar()
# entr_id=Entry(root,textvariable=var_id,font=20)
# entr_id.grid(row=0,column=1)
#
# lbl_name=Label(root,text="Enter Your Name:",font=20,bg="Yellow",width=20)
# lbl_name.grid(row=1,column=0)
# var_name=StringVar()
# entr_name=Entry(root,textvariable=var_name,font=20)
# entr_name.grid(row=1,column=1)
#
# lbl_age=Label(root,text="Enter Your Age:",font=20,bg="Yellow",width=20)
# lbl_age.grid(row=2,column=0)
# var_age=StringVar()
# entr_age=Entry(root,textvariable=var_age,font=20)
# entr_age.grid(row=2,column=1)
#
# btn_Submit=Button(root,text="Submit",font=20,width=10,height=2,bg="Orange",command=submit_Data)
# btn_Submit.grid(row=3,column=1)
#
# root.mainloop()















