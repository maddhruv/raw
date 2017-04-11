from tkinter import *

root = Tk()

one = Label(root, text="One", bg="purple", fg="pink")
one.pack()

two = Label(root, text="Two", bg="green", fg="orange")
two.pack(fill=X)#size as long as the X value is

three = Label(root, text="Three", bg="black", fg="white")
three.pack(side=LEFT, fill=Y)#fill Y

root.mainloop()
