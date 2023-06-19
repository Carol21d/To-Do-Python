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
