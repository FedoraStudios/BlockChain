from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

for i in range(0, 4):
	block_data = web3.eth.get_block(i)
	print('Block number: ', block_data['number'])
	print('Hash: ', block_data['hash'].hex())
	print('Parent hash: ', block_data['parentHash'].hex())
	print('nonce value: ', block_data['nonce'].hex())
	print('transactions: ', block_data['transactions'])
	print('-------------------')

transaction = web3.eth.get_transaction('0x26b11a61e8ffbb56c214192bfa8a6ed3f20bb71b2093085a7894c832b1b1ed02')
print('Transaction data: ', transaction)
print('To: ', transaction['to'])
print('From: ', transaction['from'])
print('Value: ', transaction['value'])
print('====================')