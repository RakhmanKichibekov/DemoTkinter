from tkinter import *


def click1():
    label1['text'] = "Выбрано: "


def click2():
    form1.destroy()


form1 = Tk()
label1 = Label(text="Выбери меню")
label1.place(x=5, y=5)
menu0 = Menu()
form1.config(menu=menu0)

menu1 = Menu(menu0, tearoff=False)
menu0.add_cascade(label="Файл", menu=menu1)
menu1.add_command(label="Открыть", command=click1)
menu1.add_separator()
menu1.add_command(label="Выход", command=click2)

menu2 = Menu(menu0, tearoff=False)
menu0.add_cascade(label="Правка", menu=menu2)
menu2.add_command(label="Копировать", command=click1)
menu2.add_separator()
menu2.add_command(label="Вставить", command=click2)

form1.mainloop()
