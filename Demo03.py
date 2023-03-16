from tkinter import *

#проект 2
form1 = Tk()
panedWindow1 = PanedWindow()
button1 = Button(text="Button1")
button2 = Button(text="Button2")
panedWindow1.add(button1)
panedWindow1.add(button2)
panedWindow1.pack()
form1.mainloop()