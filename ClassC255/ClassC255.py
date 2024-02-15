from web3 import Web3
ganache_url  = 'HTTP://127.0.0.1:7545'
web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_Account = '0x571BEdc59D7aba3576f34DE6179e501CB3bE87f4'
James_Account = '0xaC3d9d4627CacA2110Ae447A17fAC005dc082ba8'

nonce = web3_ganache_connection.eth.get_transaction_count(Alice_Account)
transaction_data = {
'nonce' : nonce,
'to' : James_Account,
'value' : web3_ganache_connection.to_wei(20, 'ether'),
'gas' : 22000,
'gasPrice' : web3_ganache_connection.to_wei(10, 'gwei')
}

private_key = '0xf0e357c98189941ef88a34b2e9d112d3190c62feb167d048caaea60e66c3c21d'
signed_transaction = web3_ganache_connection.eth.account.sign_transaction(transaction_data, private_key)
transaction_hash = web3_ganache_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
print(web3_ganache_connection.to_hex(transaction_hash))