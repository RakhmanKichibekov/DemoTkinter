from tkinter import *

def click1():
    label1['text'] = "Почём нынче луц?"

form1 = Tk()
label1 = Label(text = "Привет, пацаны!")
label1.place(x=5, y=5)
button1 = Button(text="Жмяк!", command=click1)
button1.place(x=5, y=30)
form1.mainloop()
