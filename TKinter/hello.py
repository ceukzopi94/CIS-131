from tkinter import * #imports everything from tkinter

root = Tk() #builds a root widget

#creating a label widget
myLabel = Label(root, text = "Hello World")

#shoves it in GUI in first available spot
myLabel.pack() 

root.mainloop()