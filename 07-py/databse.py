from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')

# Db
conn = sqlite3.connect("address_book.db")

# CURSOR
c = conn.cursor()

# Create table
c.exectue("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")


# Commit
conn.commit()


# close connection
conn.close()
root.mainloop()
