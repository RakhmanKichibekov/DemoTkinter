from tkinter import *

def click1():
    label1['text'] = "Выбрано: \n" + text1.get("0.0", END)

form1 = Tk()
form1.geometry("300x400+650+200")
label1 = Label(text = "Выбор")
label1.place(x=5, y=200)
text1 = Text()
text1.place(x=5,y=30, width=280, height=120)
for i in range(10):
    text1.insert("0.0", "пацак-"+str(10-i) + '\n')
button1 = Button(text="Жмяк!", command=click1)
button1.place(x=5, y=170)
form1.mainloop()
