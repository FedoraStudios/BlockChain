# --------------253 Proj----------------
from web3 import Web3
# Import time module here
import time

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Joe_account = '0x1e6c26C313ebebF28d0029eB19287268EeC4337C' #index 3
Alisa_account = '0x5D5288423EA085b01D7958F1E86Ac54e4CF183C9' #index 2 
James_account  = '0x39C437d2Dd9cc59457bcC14E0053Cb9E8D14D369' #index 1


nonce1 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data1 = {
    'nonce': James_account,
    'to': Joe_account,
    'value':web3_ganache_connection.to_wei(20, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0xde427a7c66e05ec484606b4f503a164d573f77d8378d21a246c288f4d94a9116'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash1))



# -----------------
print('Transaction in progress...')
time.sleep(5)
# -----------------

nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce': James_account,
    'to': Alisa_account,
    'value':web3_ganache_connection.to_wei(16, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0xde427a7c66e05ec484606b4f503a164d573f77d8378d21a246c288f4d94a9116'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash2))