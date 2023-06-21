from tkinter import *


class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.listbox.bind("<<ListboxSelect>>", self.on_task_selected)
        self.addButton = Button(
            self.root, text="Add Task", command=self.add_task)
        self.editButton = Button(
            self.root, text="Edit Task", command=self.edit_task)
        self.delButton = Button(
            self.root, text="Delete Task", command=self.delete_task)

        # Gui Layout
        self.entry.pack()
        self.addButton.pack()
        self.editButton.pack()
        self.listbox.pack()
        self.delButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass

    def on_task_selected(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            task = self.listbox.get(selected_index[0])
            self.entry.delete(0, END)
            self.entry.insert(END, task)

    def edit_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            edited_task = self.entry.get()
            self.listbox.delete(selected_index[0])
            self.listbox.insert(selected_index[0], edited_task)
            self.entry.delete(0, END)


root = Tk()
root.title("Python To-Do-List")
root.geometry("300x400")  # tamaño de la pantalla
to_do_list = ToDoList(root)  # llamo a mi clase
root.mainloop()
