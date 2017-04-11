from tkinter import *

root = Tk()

def hello(e):
    print("Hello")

button0 = Button(root, text="Hello")
button0.bind("<Button-1>", hello)#Button-1 => Left Click
button0.pack()

root.mainloop()
