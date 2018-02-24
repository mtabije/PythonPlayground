from tkinter import *
import sys

#Learning from https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Create Main Window
mainWindow = Tk()
mainWindow.title("Whoaaa a window")
mainWindow.geometry('400x600')

#Hello Label
howAreYou = Label(mainWindow, text="Hello", font=("Calibri", 12))
howAreYou.grid(column=0, row=0)

#Hello 2 Label
Label(mainWindow, text="Hello2", font=("Calibri", 12)).grid(column=1, row=0)


#Text Input
someText = Entry(mainWindow, width = 20)
someText.grid(column=1, row=1)

def onOkClick():
    howAreYou.configure(text = someText.get()) 
    print(someText.get())
    

#OK Button
#okButton = Button(mainWindow, text="OK", font=("Calibri", 12), command=lambda : print("ugggh")).grid(column=0, row=1)
okButton = Button(mainWindow, text="OK", font=("Calibri", 12), command=lambda : onOkClick()).grid(column=0, row=1)




#Run the GUI
mainWindow.mainloop()
