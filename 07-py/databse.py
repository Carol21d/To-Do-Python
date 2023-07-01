from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')

# Db
conn = sqlite3.connect()

# CURSOR
c = conn.cursor()

# Create table
c.exectue()


# Commit
conn.commit()


# close connection
conn.close()
root.mainloop()
