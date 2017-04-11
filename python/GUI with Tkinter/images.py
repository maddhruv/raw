from tkinter import *

root = Tk()

photo = PhotoImage(file="logo-128.png")
label = Label(root, image=photo)
label.grid(row=1, padx=10, pady=20)

root.mainloop()
