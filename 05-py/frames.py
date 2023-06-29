from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Frames')


frame = LabelFrame(root, text=" This is my frame..", padx=5, pady=5)
frame.pack(padx=100, pady=100)


b = Button(frame, text="Dont click here ")
b.pack()

root.mainloop()
