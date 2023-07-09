from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Database')
root.geometry("400x400")
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


# create submit function for database
def submit():
    # Db
    conn = sqlite3.connect("address_book.db")

    # CURSOR
    c = conn.cursor()

    # Insert into table

    c.execute(
        "INSERT INTO addresses VALUES (:f_name,:f_last,:f_address,:f_city,:f_state,:f_zipcode)",
        {

            'f_name': f_name.get(),
            'f_last': f_last.get(),
            'f_address': f_address.get(),
            'f_city': f_city.get(),
            'f_state': f_state.get(),
            'f_zipcode': f_zipcode.get()
        })
    # Commit
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    f_last.delete(0, END)
    f_address.delete(0, END)
    f_city.delete(0, END)
    f_state.delete(0, END)
    f_zipcode.delete(0, END)


def query():
    # Db
    conn = sqlite3.connect("address_book.db")

    # CURSOR
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)
    print_records
    for record in records:
        print_records += str(record) + "\n"
    query_lab = Label(root, text=print_records)

    # Commit
    conn.commit()

    # close connection
    conn.close()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
f_last = Entry(root, width=30)
f_last.grid(row=1, column=1, padx=20)
f_address = Entry(root, width=30)
f_address.grid(row=2, column=1, padx=20)
f_city = Entry(root, width=30)
f_city.grid(row=3, column=1, padx=20)
f_state = Entry(root, width=30)
f_state.grid(row=4, column=1, padx=20)
f_zipcode = Entry(root, width=30)
f_zipcode.grid(row=5, column=1, padx=20)


# Create text box labels
f_name_label = Label(root, text="First Name: ")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name: ")
l_name_label.grid(row=1, column=0)
f_address_label = Label(root, text="Address: ")
f_address_label .grid(row=2, column=0)
f_city_label = Label(root, text="City: ")
f_city_label.grid(row=3, column=0)
f_state_label = Label(root, text="State: ")
f_state_label.grid(row=4, column=0)
f_zipcode_label = Label(root, text="Zipcode: ")
f_zipcode_label.grid(row=5, column=0)


# create a submit button
submit_btn = Button(root, text="Add record to Database",
                    command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=30, ipadx=50)


# create a query button
query = Button(root, text="Show me ", command=query)
query.grid(row=7, column=0, columnspan=2, padx=20, pady=20, ipadx=137)
# Commit
conn.commit()


# close connection
conn.close()
root.mainloop()
