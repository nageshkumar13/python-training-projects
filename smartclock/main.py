# Importing necessary modules from the tkinter library and the time module
from tkinter import *
from time import *

# Function to update the time, day, and date labels
def update():
    # Get the current time in the specified format
    time_string = strftime("%I:%M:%S %p")
    # Update the text of the time label with the current time
    time_label.config(text=time_string)

    # Get the current day of the week
    day_string = strftime("%A")
    # Update the text of the day label with the current day
    day_label.config(text=day_string)

    # Get the current date in the specified format
    date_string = strftime("%B %d, %Y")
    # Update the text of the date label with the current date
    date_label.config(text=date_string)

    # Schedule the update function to be called again after 1000 milliseconds (1 second)
    window.after(1000, update)

# Create the main window
window = Tk()

# Create and configure the time label with a specified font, text color, and background color
time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
# Pack the time label into the window
time_label.pack()

# Create and configure the day label with a specified font
day_label = Label(window, font=("Cursive", 25, "bold"))
# Pack the day label into the window
day_label.pack()

# Create and configure the date label with a specified font
date_label = Label(window, font=("Ink Free", 30))
# Pack the date label into the window
date_label.pack()

# Call the update function to initialize the labels with the current time, day, and date
update()

# Start the Tkinter event loop
window.mainloop()