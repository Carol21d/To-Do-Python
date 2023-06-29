from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn Radio Button')


# r = IntVar()
# r.set(2)

MODES = [
    ("PINEAPPLE", "PINEAPPLE"),
    ("APPLE", "APPLE"),
    ("WATERMELON", "WATERMELON"),
    ("WINE", "WINE"),
]


drinks = StringVar()
drinks.set("PINEAPPLE")


for text, mode in MODES:
    Radiobutton(root, text=text, variable=drinks, value=mode).pack()


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1,
#             command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2,
#             command=lambda: clicked(r.get())).pack()


myLabel = Label(root, text=drinks.get())
myLabel.pack()


mybtn = Button(root, text="Click me !", command=lambda: clicked(drinks.get()))
mybtn.pack()
mainloop()
