from tkinter import *

root = Tk()

def hello():
    print("Hello")

button0 = Button(root, text="Hello", command=hello)
button0.pack()

root.mainloop()
