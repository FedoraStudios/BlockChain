from web3 import Web3
from web3.middleware import geth_poa_middleware

api_url = 'https://mainnet.infura.io/v3/e329224a8ca245a8af1d2c11a067f519'
web3 = Web3(Web3.HTTPProvider(api_url))

block_data = web3.eth.get_block(18735867)
transaction = web3.eth.get_transaction('0x93611268a7d1dfbbdf78370f5c2e4584008e156b0fc07ae5234604a5722a59df')

print('Block Hash: ', transaction['blockHash'].hex())
print('Block Number: ', transaction['blockNumber'])
print('from: ', transaction['from'])
print('gas: ', transaction['gas'])
print('gas price in ETH: ', transaction['gasPrice'])
print('hash: ', transaction['hash'].hex())
print('input: ', transaction['input'])
print('nonce: ', transaction['nonce'])
print('signature: ', transaction['s'].hex())
print('transaction to: ', transaction['to'])
print('value', transaction['value'])