from tkinter import *

class buttons:
    def __init__(self, master):
        frame = Frame(master, width=600, height=480)
        frame.pack()

        self.printButton = Button(frame, text="Print!", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit!", command=frame.quit)
        self.quitButton.pack(side=RIGHT)

    def printMessage(self):
        print("Hello, World!")

root = Tk()

b = buttons(root)
root.mainloop()
