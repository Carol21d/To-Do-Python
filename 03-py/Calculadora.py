from tkinter import *


root = Tk()
root.title("Simple Calculator")

# entrada de datos
entrada = Entry(root, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# funcion

def add_btn():
    return


# buttons
btn_01 = Button(root, text="1", padx=40, pady=20, command=add_btn)
btn_02 = Button(root, text="2", padx=40, pady=20, command=add_btn)
btn_03 = Button(root, text="3", padx=40, pady=20, command=add_btn)
btn_04 = Button(root, text="4", padx=40, pady=20, command=add_btn)
btn_05 = Button(root, text="5", padx=40, pady=20, command=add_btn)
btn_06 = Button(root, text="6", padx=40, pady=20, command=add_btn)
btn_07 = Button(root, text="7", padx=40, pady=20, command=add_btn)
btn_08 = Button(root, text="8", padx=40, pady=20, command=add_btn)
btn_09 = Button(root, text="9", padx=40, pady=20, command=add_btn)
btn_00 = Button(root, text="0", padx=40, pady=20, command=add_btn)
btn_Equals = Button(root, text="=", padx=40, pady=20, command=add_btn)
btn_Clear = Button(root, text="C", padx=40, pady=20, command=add_btn)
btn_Subs = Button(root, text="+", padx=40, pady=20, command=add_btn)
btn_Rest = Button(root, text="-", padx=40, pady=20, command=add_btn)
btn_Multi = Button(root, text="x", padx=40, pady=20, command=add_btn)
btn_Div = Button(root, text="%", padx=40, pady=20, command=add_btn)


# ordenando los buttons en la pantalla
btn_09.grid(row=1, column=2)
btn_08.grid(row=1, column=1)
btn_07.grid(row=1, column=0)
btn_06.grid(row=2, column=2)
btn_05.grid(row=2, column=1)
btn_04.grid(row=2, column=0)
btn_03.grid(row=3, column=2)
btn_02.grid(row=3, column=1)
btn_01.grid(row=3, column=0)
btn_00.grid(row=4, column=1)
btn_Equals.grid(row=4, column=0)
btn_Clear.grid(row=4, column=2)
btn_Subs.grid(row=1, column=3)
btn_Rest.grid(row=2, column=3)
btn_Multi.grid(row=3, column=3)
btn_Div.grid(row=4, column=3)


root.mainloop()
