from tkinter import *
from PIL import ImageTk, Image
# pil is to import images to python
root = Tk()

root.title("Learning to Code")
root.iconbitmap('/Users/orlandouchiha/sdev140/module5/pigicon.ico')


my_img = ImageTk.PhotoImage(Image.open("goku.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text=" Exit Program", command=root.quit)

button_quit.pack()
root.mainloop()
