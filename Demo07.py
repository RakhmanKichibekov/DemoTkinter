from tkinter import *

from Demo07U import f


def click1():
    label1['text'] = "Результат: " + str(f(2, 3))


form1 = Tk()
label1 = Label(text="Считаем")
label1.place(x=5, y=5)
button1 = Button(text="Жмяк!", command=click1)
button1.place(x=5, y=30)
form1.mainloop()
