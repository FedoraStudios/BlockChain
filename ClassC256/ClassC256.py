from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/e329224a8ca245a8af1d2c11a067f519'
web3_infura_connection = Web3(Web3.HTTPProvider(infura_url))

Account1 = '0x970e07Ce87ffDB7cf1B9a5Cc5F98f0545f38d064'
Account2 = '0x0C5dE2F3F12C9DC4F8dDA8b31248CfdACDcDc14a'
Private_Key = 'bdf8c317287daef06dffd4ec8417a30c43a58cd51b72f3f0db00235c50e6e69c'

nonce = web3_infura_connection.eth.get_transaction_count(Account1)
transaction_data = {
'nonce' : nonce,
'to' : Account2,
'value' : web3_infura_connection.to_wei(0.0001, 'ether'),
'gas' : 21000,
'gasPrice' : web3_infura_connection.to_wei(10, 'gwei')
}

signed_transaction = web3_infura_connection.eth.account.signed_transaction(transaction_data.Private_Key)
transaction_hash = web3_infura_connection.eth.send_raw_transaction(signed_transaction.raw_transaction)
print(web3_infura_connection.to_hex(transaction_hash))