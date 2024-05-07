# Import necessary modules from the tkinter library
import tkinter
from tkinter import *

# Create the main Tkinter window
root = Tk()

# Set the title, size, and position of the window
root.title("To-Do List")
root.geometry("400x650+1000+100")
root.resizable(False, False)

# Initialize an empty list to store tasks
task_list = []

# Function to add a task to the list and update the GUI
def addTask():
    # Get the task from the entry widget
    task = task_entry.get()
    # Clear the entry widget
    task_entry.delete(0, END)

    if task:
        # Append the task to the task list and update the file
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        # Update the list box
        list_box.insert(END, task)

# Function to delete a selected task from the list and update the GUI
def deleteTask():
    global task_list
    # Get the selected task from the list box
    task = str(list_box.get(ANCHOR))
    if task in task_list:
        # Remove the task from the task list
        task_list.remove(task)
        # Update the file with the modified task list
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        # Remove the task from the list box
        list_box.delete(ANCHOR)

# Function to open and load tasks from the tasklist.txt file
def openTaskFile():
    try:
        global task_list
        # Read tasks from the file
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        # Add tasks to the task list and update the list box
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                list_box.insert(END, task)
    except FileNotFoundError:
        # If the file is not found, create an empty file
        file = open("tasklist.txt", "w")
        file.close()

# Set up the window icon and header images
Image_icon = PhotoImage(file="images/todo.png")
root.iconphoto(False, Image_icon)

header_image = PhotoImage(file="images/nyt.png")
Label(root, image=header_image, height=50).pack()

docu_image = PhotoImage(file="images/4388473.png")
Label(root, image=docu_image, bg="#E1AA74").place(x=10, y=1)

# Set up the main heading of the application
heading = Label(root, text="Tasks to do", font="cursive 20 bold", fg="#FFFADD", bg="#0B60B0")
heading.place(x=120, y=10)

# Create a frame for the task entry and add button
frame = Frame(root, width=400, height=50, bg="#FFFADD")
frame.place(x=0, y=180)

# Create an Entry widget for entering tasks
task = StringVar()
task_entry = Entry(frame, width=20, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Create an "ADD" button with the addTask function
button = Button(frame, text="ADD", font="arial 20 bold", fg="white", bg="#40A2D8", bd=0, command=addTask)
button.place(x=320, y=0)

# Create a frame for the task list and scrollbar
frame1 = Frame(root, bd=3, width=700, height=280, bg="#0B60B0")
frame1.pack(pady=(190, 0))

# Create a Listbox for displaying tasks
list_box = Listbox(frame1, font="arial, 20", width=25, height=10, bg="#0B60B0", fg="white", cursor="hand2",
                   selectbackground="lightblue")
list_box.pack(side=LEFT, fill=BOTH, padx=4)

# Create a Scrollbar for the list box
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

# Configure the list box to use the scrollbar
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

# Load tasks from the file when the application starts
openTaskFile()

# Set up the delete button with the deleteTask function
delete_image = PhotoImage(file="images/del.png")
Button(root, image=delete_image, bd=0, command=deleteTask).pack(side=BOTTOM, pady=10)

# Start the Tkinter main loop
root.mainloop()