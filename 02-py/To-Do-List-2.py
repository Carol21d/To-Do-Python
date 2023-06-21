from tkinter import *


root = Tk()
# create a label widget
# myLabel = Label(root, text="Hello World!!")
# myLabel2 = Label(root, text="Hola Mundo")
# showing it into the screen
# myLabel.pack()
# redisize las labels
# myLabel.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)


# creamos una funcion
def _click_btn():
    mylabel = Label(root, text="Haz hecho click en el boton")
    mylabel.pack()


# creating buttons
myBtn = Button(root, text="Click here", command=_click_btn)
myBtn.pack()


root.mainloop()
