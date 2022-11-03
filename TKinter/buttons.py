from tkinter import * #imports everything from tkinter

root = Tk() #builds a root widget

def myClick():
    myLabel = Label(root, text="Look i clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()

root.mainloop()