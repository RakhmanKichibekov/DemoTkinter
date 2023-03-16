from tkinter import *

#проект 1
def click1():
    label1['text'] = entry1.get()

form1 = Tk()
label1 = Label(text = "Что скажешь?")
label1.place(x = 1, y = 1)
entry1 = Entry()
entry1.place(x=23,y=23)
entry1.insert(0,"у вас есть кц?")
button1 = Button(text="Жмяк!", command = click1).place(x=50,y=50)
#button1.place(x = 5,y = 10)
form1.mainloop()




