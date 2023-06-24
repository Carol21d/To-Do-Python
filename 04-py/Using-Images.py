from tkinter import *
from PIL import IamgeTk, Image


root = Tk()
root.title("Learn to Python")
# root.iconbitmap('c:/gui/codemy.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
