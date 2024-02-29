from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Cryptic')
root.configure(bg = 'grey')

imageLogo = ImageTk.PhotoImage(Image.open('logo.jpeg'))
imagelogoLabel = Label(root, image = imageLogo)

imagelogoLabel.pack(side = 'top')
frame = Frame(root, bg = 'grey', padx = 5, pady = 5)

Label(frame, text = 'Account Number One: ', fg = 'black', bg = 'white').grid(row = 0, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number Two: ', fg = 'black', bg = 'white').grid(row = 1, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Private Key: ', fg = 'black', bg = 'white').grid(row = 2, column = 0, sticky = W, pady = 10)
Label(frame, text = 'ETH: ', fg = 'black', bg = 'white').grid(row = 3, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Price (Gwei): ', fg = 'black', bg = 'white').grid(row = 4, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Limit (Gwei): ', fg = 'black', bg = 'white').grid(row = 5, column = 0, sticky = W, pady = 10)

frame.pack()

root.mainloop()