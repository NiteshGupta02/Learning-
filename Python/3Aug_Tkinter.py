""
"""
tkinter continue
CMS using OOPS

"""

"""
How to handle the events: 


"""
# from tkinter import *
# def left_Click():
#     print("Thanks for left click.")
# def right_Click(e):
#     print("Thanks for right click.")
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="Submit",font=20,command=left_Click)
# btn.bind("<Button-3>",right_Click)
# btn.pack()
# root.mainloop()

# #New Program
# from tkinter import *
# def left_Click(e):
#     print("Thanks for left click.")
#     btn["bg"]="Yellow"
# def right_Click(e):
#     print("Thanks for right click.")
#     btn["bg"]="White"
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="Submit",font=20)
# btn["height"]=4
# btn["width"]=20
# btn.bind("<Button-1>",left_Click)
# btn.bind("<Button-3>",right_Click)
# btn.pack()
# root.mainloop()

# #New Program
# from tkinter import *
# def left_Click(e):
#     print(e.x,e.y)
#     print(e.widget)
#     print("Thanks for left click.")
#     btn["bg"]="Yellow"
# def right_Click(e):
#     print("Thanks for right click.")
#     btn["bg"]="White"
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="Submit",font=20)
# print(btn)
# btn["height"]=4
# btn["width"]=20
# btn.bind("<Button-1>",left_Click)
# btn.bind("<Button-3>",right_Click)
# btn.pack()
# root.mainloop()


#New Program
from tkinter import *
def upHandler(e):
    global a,b
    b-=10
    move_btn.place(x=a,y=b)
def downHandler(e):
    global a,b
    b+=10
    move_btn.place(x=a,y=b)
def leftHandler(e):
    global a,b
    a-=10
    move_btn.place(x=a,y=b)
def rightHandler(e):
    global a,b
    a+=10
    move_btn.place(x=a,y=b)



root=Tk()
root.geometry("500x500")
a,b=200,200
move_btn=Button(root,text="Move Button",font=20)
move_btn.place(x=a,y=b)
root.bind("<Up>",upHandler)
root.bind("<Down>",downHandler)
root.bind("<Left>",leftHandler)
root.bind("<Right>",rightHandler)
root.mainloop()

