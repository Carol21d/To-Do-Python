from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')

# Db
conn = sqlite3.connect()

# CURSOR
c = conn.cursor()


# Commit
conn.commit()

root.mainloop()
