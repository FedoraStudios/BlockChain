from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('FrameDemo')

frame = Frame(root, bg = 'grey', padx = 5, pady = 5)

image1 = ImageTk.PhotoImage(Image.open('E.jpg'))
image2 = ImageTk.PhotoImage(Image.open('t.jpg'))
image3 = ImageTk.PhotoImage(Image.open('OIP.jpg'))
image4 = ImageTk.PhotoImage(Image.open('w.jpg'))

image1Label = Label(frame, image = image1).grid(row = 0, column = 0)
image2Label = Label(frame, image = image2).grid(row = 0, column = 1)
image3Label = Label(frame, image = image3).grid(row = 1, column = 0)
image4Label = Label(frame, image = image4).grid(row = 1, column = 1)

frame.pack()

root.mainloop()