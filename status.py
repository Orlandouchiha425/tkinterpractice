from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')


my_img1 = ImageTk.PhotoImage(Image.open("image/goku.png"))
my_img2 = ImageTk.PhotoImage(Image.open("image/vegeta.png"))
my_img3 = ImageTk.PhotoImage(Image.open("image/goku.png"))
my_img4 = ImageTk.PhotoImage(Image.open("image/vegeta.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]
status = Label(root, text="image 1 of " +
               str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
# anchor sets our status all the way to right
# SUNKEN is so the button is deepen/sunken, bd is the border
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text="image " + str(image_number) + " of " +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # update status bar
    status = Label(root, text="image " + str(image_number) + " of " +
                   str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
# pady gives space betwen the "status" and exit program button
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
# sticky is set to west to east it stretches our status bar left to right
root.mainloop()
