from tkinter import * #imports everything from tkinter

root = Tk() #builds a root widget

#creating a label widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My Name Is Christian Urbanski")

#shoves it in GUI on a r & c grid
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0) 

root.mainloop()