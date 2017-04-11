from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Windows Title', 'This is a message box!!')

answer = tkinter.messagebox.askquestion("Question", "Yes / NO?")

if answer == "yes":
    print(":==)")

root.mainloop()
