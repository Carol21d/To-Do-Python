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
# c.execute("""CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")


f_name = Entry(root, width=30)
f_name.grid(row=0, column=0, padx=20)

f_last = Entry(root, width=30)
f_last.grid(row=0, column=0, padx=20)

f_address = Entry(root, width=30)
f_address.grid(row=0, column=0, padx=20)

f_city = Entry(root, width=30)
f_city.grid(row=0, column=0, padx=20)


f_state = Entry(root, width=30)
f_state.grid(row=0, column=0, padx=20)

f_zipcode = Entry(root, width=30)
f_zipcode.grid(row=0, column=0, padx=20)

# Commit
conn.commit()


# close connection
conn.close()
root.mainloop()
