#import libraries
from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Valentine Date Proposal")

#label to prompt user for name variable
label = tk.Label(root, text="Enter your name below!", font="Helvetica 15")
label.pack()

entry = Entry(root, width=25)
entry.pack()

#setting window size
root.geometry("500x500")
root.config(bg="#111")

# Load the image saved in the file
image = PhotoImage(file="vallove.png")


# Create a label to display the image
label = tk.Label(root, image=image)
label.pack()

#function for event upon clicking the button
def onClick():
    name = entry.get()
    tkinter.messagebox.showinfo(name + ", be my date tonight .........")
#creating the button
button = Button(root, text="Click Me Baby", command=onClick, height=3, width=17)
# Set the position of button on the top of window.
button.pack(side='bottom')

root.mainloop()
