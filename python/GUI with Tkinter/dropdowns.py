from tkinter import *

def hello():
    print("Hello!")

root = Tk()

menuBar = Menu(root, fg="white", bg="black")#main menu
root.config(menu=menuBar)

subMenu = Menu(menuBar, fg="white", bg="black")
menuBar.add_cascade(label="File", menu=subMenu)#funcionality

subMenu.add_command(label="New", command=hello)
subMenu.add_command(label="Save", command=hello)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menuBar, fg="white", bg="black")
menuBar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut", command=hello)

root.mainloop()
