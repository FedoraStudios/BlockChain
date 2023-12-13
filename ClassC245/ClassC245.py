from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/e329224a8ca245a8af1d2c11a067f519'
web3 = Web3(Web3.HTTPProvider(infura_url))
gas_prices = web3.eth.gas_price

#Calculating gas prices at different levels
safe_low_gas_price = int(gas_prices*0.9) #90% of current gas prices
average_gas_price = int(gas_prices*1.0) #Same as the current gas price
fast_gas_price = int(gas_prices*1.1) #110% of current gas prices
fastest_gas_price = int(gas_prices*1.2) #120% of current gas prices

#Converting gas prices fro Wei to GWei
safe_low_gas_price_GWei = web3.from_wei(safe_low_gas_price, 'gwei')
average_gas_price_GWei = web3.from_wei(average_gas_price, 'gwei')
fast_gas_price_GWei = web3.from_wei(fast_gas_price, 'gwei')
fastest_gas_price_GWei = web3.from_wei(fastest_gas_price, 'gwei')

print('Safe low gas price (GWei): ', safe_low_gas_price_GWei)
print('Average low gas price (Gwei): ', average_gas_price_GWei)
print('Fast gas price (GWei): ', fast_gas_price_GWei)
print('Fastest gas price (Gwei):', fastest_gas_price_GWei)

gas_price = web3.eth.gas_price
print('Gas Price in GWei: ', gas_prices)