from tkinter import *


root = Tk()

# entrada de datos
entrada = Entry(root, width=20)
entrada.pack()

# buttons
btn_01 = Button(root, text="1")
btn_01.pack()
btn_02 = Button(root, text="2")
btn_02.pack()
btn_03 = Button(root, text="3")
btn_03.pack()
btn_04 = Button(root, text="4")
btn_04.pack()
btn_05 = Button(root, text="5")
btn_05.pack()
btn_06 = Button(root, text="6")
btn_06.pack()
btn_07 = Button(root, text="7")
btn_07.pack()
btn_08 = Button(root, text="8")
btn_08.pack()
btn_09 = Button(root, text="9")
btn_09.pack()
btn_00 = Button(root, text="0")
btn_00.pack()
btn_Equals = Button(root, text="=")
btn_Equals.pack()
btn_Clear = Button(root, text="Clear")
btn_Clear.pack()
btn_Subs = Button(root, text="+")
btn_Subs.pack()
btn_Rest = Button(root, text="-")
btn_Rest.pack()
btn_Multi = Button(root, text="x")
btn_Multi.pack()
btn_Div = Button(root, text="%")
btn_Div.pack()


root.mainloop()
