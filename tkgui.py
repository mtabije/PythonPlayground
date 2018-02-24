from tkinter import *
import sys

mainWindow = Tk()

mainWindow.title("Whoaaa a window")
mainWindow.geometry('400x600')

#Hello Label
howAreYou = Label(mainWindow, text="Hello", font=("Calibri", 12))
howAreYou.grid(column=0, row=0)

#Hello 2 Label
Label(mainWindow, text="Hello2", font=("Calibri", 12)).grid(column=2, row=0)

#OK Button
okButton = Button(mainWindow, text="OK", font=("Calibri", 12), command=lambda : print("ugggh")).grid(column=0, row=1)
mainWindow.mainloop()
