from web3 import Web3
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

accountOne = '0xf31b9F642Bc5656b283F2E588DEAD491a92a88CC'
accountTwo = '0x33FAA4B99e6d12Fd2899fb382eB37b0e369Cdbe2'

private_key = '0x309d4343434f06fba12e34a34185a086e12e8fd342575c79ed93bec3e7fa0a25'
nonce = web3.eth.get_transaction_count(accountOne)

tx = {
'nonce' : nonce,
'to' : accountTwo,
'value' : web3.to_wei(1, 'ether'),
'gas' : 21000,
'gasPrice' : web3.to_wei(50, 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.to_hex(tx_hash))