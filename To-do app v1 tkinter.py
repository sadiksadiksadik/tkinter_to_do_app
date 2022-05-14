import tkinter as tk
import tkinter.messagebox
import pickle


# Init display window
root = tk.Tk()
root.title('The Fox to-do app v1')
root.geometry('1000x1000')
root.configure(bg='#000000')

# Function to add task to listbox of tasks
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, '-------------------------------------------------------------', 
                                task, '-------------------------------------------------------------')
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
the_task_frame.config(bg='#000000')
the_task_frame.pack()
the_task_frame.config(bg='#000000')

# List of Tasks
tasks_listbox = tk.Listbox(the_task_frame, font=('Terminal', 18), height=20, width=300)
tasks_listbox.pack(side=tk.LEFT)
tasks_listbox.configure(bg='#000000')
tasks_listbox.configure(fg='#FFFFF0')
tasks_listbox.configure(activestyle='none')

# Scrollbar
scrollbar = tk.Scrollbar(the_task_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Task Text Entry Form
task_entry = tk.Entry(root, text='Add tasks here', width=300)
task_entry.pack(fill=tk.Y)
task_entry.configure(bg='#000000')
task_entry.configure(fg='#FFFFF0')
task_entry.configure( font=('Terminal', 18))


# The Add Task Button
add_task_button = tk.Button(root, text='Add task', font=('Terminal'), height=3, width=300, command=add_task)
add_task_button.config(activebackground='#000000')
add_task_button.pack()
add_task_button.configure(bg='#000000')
add_task_button.configure(fg='#FFFFF0')

# The Delete Task Button
delete_task_button = tk.Button(root, text='Delete task', font=('Terminal'), height=3, width=300, command=delete_task)
delete_task_button.config(activebackground='#F0FFFF')
delete_task_button.pack()
delete_task_button.configure(bg='#000000')
delete_task_button.configure(fg='#FFFFF0')

# The Load Tasks Button
load_task_button = tk.Button(root, text='Load tasks', font=('Terminal'), height=3, width=300, command=load_task)
load_task_button.config(activebackground='#F0FFFF')
load_task_button.pack()
load_task_button.configure(bg='#000000')
load_task_button.configure(fg='#FFFFF0')

# The Save Tasks Button
save_task_button = tk.Button(root, text='Save tasks', font=('Terminal'), height=3, width=300, command=save_task)
save_task_button.config(activebackground='#F0FFFF')
save_task_button.pack()
save_task_button.configure(bg='#000000')
save_task_button.configure(fg='#FFFFF0')

root.mainloop()

