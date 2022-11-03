from tkinter import * #imports everything from tkinter

root = Tk() #builds a root widget

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()

    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Name", command=myClick)
myButton.pack()

root.mainloop()