from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

line = canvas.create_line(0, 200, 400, 400)
redline = canvas.create_line(0, 400, 400, 200, fill="red")
greenline = canvas.create_line(0, 400, 200, 0, fill="green")
blueline = canvas.create_line(200, 0, 400, 400, fill="blue")
yellowline = canvas.create_line(0, 200, 400, 200, fill="yellow")

orangebox = canvas.create_rectangle(100, 20, 10, 10, fill="blue")

root.mainloop()
