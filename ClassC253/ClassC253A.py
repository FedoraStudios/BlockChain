from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3_ganache_conection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0xEF87380fEf7ae3b3cdB128DD1Ab4DB377Ad70cAC'
James_account = '0x39C437d2Dd9cc59457bcC14E0053Cb9E8D14D369'

nonce = web3_ganache_conection.eth.get_transaction_count(Alice_account)

transaction_data = {
'nonce' : nonce,
'to' : James_account,
'value' : web3_ganache_conection.to_wei(10, 'ether'),
'gas' : 21000,
'gasPrice' : web3_ganache_conection.to_wei(50, 'gwei'),
}

private_key = '0xe6dff74749c715f00693bac7bf038eb4edf4dace8fc4c4e1d12b20804dd64542'
sign_transaction = web3_ganache_conection.eth.account.sign_transaction(transaction_data, private_key)
transaction_hash = web3_ganache_conection.eth.send_raw_transaction(sign_transaction.rawTransaction)

print(web3_ganache_conection.to_hex(transaction_hash))