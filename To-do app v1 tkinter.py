import tkinter as tk
import tkinter.messagebox
import pickle


# Init display window
root = tk.Tk()
root.title('The Fox to-do app v1')
# root.geometry('600x600')
root.configure(bg='#F0FFFF')

# Function to add task to listbox of tasks
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title='Warning', message='You must enter a task')
 
#  Function to delete a task from the listbox of tasks       
def delete_task():
    try:
        task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(task_index)
    except:
        tk.messagebox.showwarning(title='warning', message='you must select a task')

# Load Task from Disk
def load_task():
    try:
        tasks = pickle.load(open('tasks.dat', 'rb'))
        tasks_listbox.delete(0, tk.END)
        for task in tasks:
            tasks_listbox.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(title='warning!', message='cannot find tasks.dat')
    

# Save Task to Disk
def save_task():
    tasks = tasks_listbox.get(0, tasks_listbox.size())
    pickle.dump(tasks, open('tasks.dat', 'wb'))



# Create The GUI

# Frame Box for Scroll Bar and Listbox
the_task_frame = tk.Frame(root)
the_task_frame.pack()

# List of Tasks
tasks_listbox = tk.Listbox(the_task_frame, font=('Calibri', 20, 'italic'), height=14, width=300)
tasks_listbox.pack(side=tk.LEFT)
tasks_listbox.configure(bg='#F5F5DC')

# Scrollbar
scrollbar = tk.Scrollbar(the_task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Task Text Entry Form
task_entry = tk.Entry(root, width=300)
task_entry.pack()

# The Add Task Button
add_task_button = tk.Button(root, text='Add task', width=300, command=add_task)
add_task_button.config(activebackground='#F0FFFF')
add_task_button.pack(expand=True)

# The Delete Task Button
delete_task_button = tk.Button(root, text='Delete task', width=300, command=delete_task)
delete_task_button.config(activebackground='#F0FFFF')
delete_task_button.pack()

# The Load Tasks Button
load_task_button = tk.Button(root, text='Load tasks', width=300, command=load_task)
load_task_button.config(activebackground='#F0FFFF')
load_task_button.pack()

# The Save Tasks Button
save_task_button = tk.Button(root, text='Save tasks', width=300, command=save_task)
load_task_button.config(activebackground='#F0FFFF')
save_task_button.pack()

root.mainloop()

