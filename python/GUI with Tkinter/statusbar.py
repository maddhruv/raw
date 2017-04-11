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


toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Insert Image", command=hello)
insertButton.pack(side=LEFT, padx=2, pady=2)

printButton = Button(toolbar, text="button", command=hello)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


status = Label(root, text="File Open", bd=1, relief=SUNKEN, anchor=W)#bd=border #relief=feels inset
status.pack(side=BOTTOM, fill=X)

root.mainloop()
