from tkinter import *

root = Tk()

name = Label(root, text="Username")
password = Label(root, text="Password")

entryName = Entry(root)
entryPassword = Entry(root)

name.grid(row=0, sticky=W)#by default column is 0
#sticky => N=North, E=East, S=South, W=West
password.grid(row=1, sticky=W)

entryName.grid(row=0, column=1)
entryPassword.grid(row=1, column=1)

checkButton = Checkbutton(root, text="Keep me Logged in")#radio button
checkButton.grid(columnspan=2)#column width

loginButton = Button(root, text="Login")
loginButton.grid(row=3, columnspan=2)

root.mainloop()
