from tkinter import *

root = Tk()

def left(e):
    print("Left")

def right(e):
    print("Right")

def middle(e):
    print("Middle")

frame = Frame(root, width=300, height=230)
frame.bind("<Button-1>", left)#left button
frame.bind("<Button-2>", middle)#middle button
frame.bind("<Button-3>", right)#right button
frame.pack()

root.mainloop()
