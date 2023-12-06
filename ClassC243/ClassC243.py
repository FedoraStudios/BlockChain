from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/d4dcfb3c4d134fb98f94fd33519131d6'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.get_block(18728748)
print('Block data: ', Block_data)
print('Gas used: ', Block_data['gasUsed'])
print('Total Difficulty: ', Block_data['difficulty'])
print('Transaction data: ', Block_data['transactions'])

transaction = web3.eth.get_transaction('0x24e562f869091f606e6547e7391dfbf6a76eb9836b6c88ffe1033f04cc969260')
print('data: ', transaction)
