from web3 import Web3
import json
import requests

url = 'https://mainnet.infura.io/v3/e329224a8ca245a8af1d2c11a067f519'
web3 = Web3(Web3.HTTPProvider(url))

#req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json') #obtaining the data from the api using the json format
#latest_block_info = json.loads(req_ethgas_data.content) #Converting the json data into normal data

#accesing the various costs of transactions depending on the speed
#print('Safe low: ', latest_block_info['safeLow'])
#print('Average: ', latest_block_info['average'])
#print('Fast: ', latest_block_info['fast'])
#print('Fastest: ', latest_block_info['fastest'])
#print('Block number: ', latest_block_info['blockNum'])

#converting gas price into ETH and USD
gas_price = web3.eth.gas_price
gas_price_in_eth = gas_price/10**18
print('Gas price in ETH: ', gas_price_in_eth)

gas_price_in_USD = gas_price_in_eth*3105.35
print('Gas price in USD: ', gas_price_in_USD)

block_data = web3.eth.get_block(18785797)
latest_transaction = block_data['transactions'][-1].hex()
print('Transaction hash data: ', latest_transaction)

transaction_detail = web3.eth.get_transaction(latest_transaction)
gas_estimate = web3.eth.estimate_gas({'to': transaction_detail['to'], 'from': transaction_detail['from']})
print('Gas used in this transaction is: ', gas_estimate)
print('Gas limit is: ', transaction_detail['gas'])