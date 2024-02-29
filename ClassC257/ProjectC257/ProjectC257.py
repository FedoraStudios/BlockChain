from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='grey')
panel.pack(side="top")

frame = Frame(
    root,
    bg='grey',
    padx=5,
    pady=5
)

Label(frame, text = 'Account Number Zero', fg = 'black', bg = 'white').grid(row = 0, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number One', fg = 'black', bg = 'white').grid(row = 1, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number Two', fg = 'black', bg = 'white').grid(row = 2, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number Three', fg = 'black', bg = 'white').grid(row = 3, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number Four', fg = 'black', bg = 'white').grid(row = 4, column = 0, sticky = W, pady = 10)

accountZero = Entry(frame).grid(row = 0, column = 1, padx = 20, pady = 10)
accountOne = Entry(frame).grid(row = 1, column = 1, padx = 20, pady = 10)
accountTwo = Entry(frame).grid(row = 2, column = 1, padx = 20, pady = 10)
accountThree = Entry(frame).grid(row = 3, column = 1, padx = 20, pady = 10)
accountFour = Entry(frame).grid(row = 4, column = 1, padx = 20, pady = 10)

result = Text(root, height = 10, width = 45, bg = 'white')

#define a function CHECK_BALANCE() and add the code inside it.
def CheckBalance():

    accountNumber = []
    accountNumber.append(accountZero.get())
    accountNumber.append(accountOne.get())
    accountNumber.append(accountTwo.get())
    accountNumber.append(accountThree.get())
    accountNumber.append(accountFour.get())

    count = 0
    for i in accountNumber:
        balance = web3.eth.getBalance(i)
        balance = balance * 0.000000000000000001
        result.insert(END, f'account: {count} balance: {balance} \n')
        count = count+1

frame.pack()

Button(root, width = 15, text = 'Check Balance', command = CheckBalance)
Button.pack()

result.pack(pady=5)
root.mainloop()
