from tkinter import *


def click1(e):
    label1['text'] = "Мой выбор: " + listbox1.get(listbox1.curselection())


form1 = Tk()
label1 = Label(text="Выбери девушку")
label1.place(x=5, y=5)
listMyGirls = ["Вероника", "Ануш", "Мадина", "Ангелина", "Зоя", "Анна", "Василиса"]
listbox1 = Listbox(listvariable=Variable(value=listMyGirls))
listbox1.place(x=5, y=30)
listbox1.bind("<<ListboxSelect>>", click1)
form1.mainloop()
