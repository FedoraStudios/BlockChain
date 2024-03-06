from tkinter import *
from tkinter import messagebox
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title('Cryptic')
root.configure(bg = 'grey')

infura_URL = 'https://mainnet.infura.io/v3/e329224a8ca245a8af1d2c11a067f519'
web3_infura_connection = Web3(Web3.HTTPProvider(infura_URL))

image_logo = ImageTk.PhotoImage(Image.open('logo.jpeg'))
image_label = Label(root, image = image_logo, bg = 'grey')
image_label.pack(side = 'top')

frame = Frame(root, bg = 'grey', padx = 5, pady = 5)

Label(frame, text = 'Account Number One: ', fg = 'black', bg = 'white').grid(row = 0, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Account Number Two: ', fg = 'black', bg = 'white').grid(row = 1, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Private Key: ', fg = 'black', bg = 'white').grid(row = 2, column = 0, sticky = W, pady = 10)
Label(frame, text = 'ETH: ', fg = 'black', bg = 'white').grid(row = 3, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Price (Gwei): ', fg = 'black', bg = 'white').grid(row = 4, column = 0, sticky = W, pady = 10)
Label(frame, text = 'Gas Limit (Gwei): ', fg = 'black', bg = 'white').grid(row = 5, column = 0, sticky = W, pady = 10)

AccountOne = Entry(frame)
AccountTwo = Entry(frame)
PrivateKey = Entry(frame)
Amount = Entry(frame)
GasPrice = Entry(frame)
GasLimit = Entry(frame)

AccountOne.grid(row = 0, column = 1, pady = 10, padx = 20)
AccountTwo.grid(row = 1, column = 1, pady = 10, padx = 20)
PrivateKey.grid(row = 2, column = 1, pady = 10, padx = 20)
Amount.grid(row = 3, column = 1, pady = 10, padx = 20)
GasPrice.grid(row = 4, column = 1, pady = 10, padx = 20)
GasLimit.grid(row = 5, column = 1, pady = 10, padx = 20)

def SendETH():
	AccountOneID = AccountOne.get()
	AccountTwoID = AccountTwo.get()
	Key = PrivateKey.get()
	AmountETH = Amount.get()
	GasFee = GasPrice.get()
	Glimit = GasLimit.get()

	nonce = web3_infura_connection.eth.get_transaction_count(AccountOneID)
	transaction = {
	'nonce' : nonce,
	'to' : AccountTwoID,
	'value' : web3_infura_connection.to_wei(AmountETH, 'ether'),
	'gas' : int(Glimit),
	'gasPrice' : web3_infura_connection.to_wei(GasFee, 'gwei')
	}

	signed_transaction = web3_infura_connection.eth.account.sign_transaction(transaction, Key)
	transaction_hash = web3_infura_connection.eth.send_raw_transaction(signed_transaction, raw_transaction)
	print('Your transaction was succesful, your transaction ID is: ', transaction_hash.hex())
	messagebox.showinfo('Transaction status', 'Transaction Succesful, verify your wallet.')

frame.pack()
transfer_eth = Button(root, text = 'Transfer ETH', command = SendETH, highlightbackground = 'white', width = 15)
transfer_eth.pack

root.mainloop()