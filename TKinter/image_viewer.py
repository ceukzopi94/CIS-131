from cProfile import label
from glob import glob
from operator import indexOf
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code')
#root.iconbitmap('C:/Users/ceukz/Desktop/Pima/CIS 131/TKinter/test.ico') #full path not needed
# full path not needed if in the same folder
root.iconbitmap('C:/Users/ceukz/Desktop/Pima/CIS 131/TKinter/images collection/mario.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images collection/cool glasses.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images collection/butterfly.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images collection/spongebob.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images collection/unifrog.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images collection/world outline.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[img_num - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(img_num - 1))
    
    if img_num == 5:
        button_forward = Button(root, text = ">>", state = DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num - 1])

    button_forward = Button(root, text=">>", command=lambda: forward(img_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(img_num - 1))

    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command= back, state = DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="EXIT", command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()