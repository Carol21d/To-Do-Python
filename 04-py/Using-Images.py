from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to Python")
root.iconbitmap('C:/Users/d3sig/OneDrive/Desktop/Projects-Python')

my_img = ImageTk.PhotoImage(Image.open("lizard.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
