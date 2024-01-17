import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List in Python Programming")

        # Area for Task entry
        self.task_entry = tk.Entry(root, width=50, bg="turquoise")
        self.task_entry.grid(row=1, column=1, padx=10, pady=10)

        # Area to Add task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="Lightgreen")
        add_button.grid(row=0, column=2, padx=10, pady=10)

        # Area for Task listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10, bg="coral")
        self.task_listbox.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

        # Area to Remove task button
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="Salmon")
        remove_button.grid(row=0, column=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Alert...!!!!", "Enter a task to be performed.")

    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            self.task_listbox.delete(selected_task)
        else:
            messagebox.showwarning("Alert...!!!!", "Select a task that you wish to remove.")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()