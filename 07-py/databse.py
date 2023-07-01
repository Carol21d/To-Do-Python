from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')


conn = sqlite3.connect()
root.mainloop()
