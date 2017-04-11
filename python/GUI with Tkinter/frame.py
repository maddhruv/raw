from tkinter import *

root = Tk()#main window

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button0 = Button(topFrame, text="Button 0", fg="black")
button1 = Button(topFrame, text="Button 1", fg="black")
button2 = Button(topFrame, text="Button 2", fg="black")

button3 = Button(bottomFrame, text="Button 3", fg="blue")
button4 = Button(bottomFrame, text="Button 4", fg="cyan")

button0.pack(side=LEFT)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()#doesnt close
