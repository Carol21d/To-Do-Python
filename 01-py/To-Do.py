from tkinter import *


class ToDoList:
    def _init_(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self, root)
        self.entry = Entry(self, root)
        self.addButton = Button(
            self, root, text="Add Task", command=self.add_task)
        self.delButton = Button(
            self, root, text="Delete Task", command=self.delete_task)

        # Gui Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != " ":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)
