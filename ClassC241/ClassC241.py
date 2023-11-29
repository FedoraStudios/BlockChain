import hashlib
import json
from time import time

class Block:
	def __init__(self):
		self.chain = []
		self.new_transactions = []
		self.count = 0
		self.new_block(previous_hash = 'No previous hash since this is the first one.')

	def new_block(self, previous_hash = None):
		block = {
		'block_number' : self.count,
		'timestamp' : time(),
		'transactions' : self.new_transactions or 'No transactions, first genecis block.',
		'gas_fee' : 0.01,
		'previous_hash' : previous_hash,
		}
		self.count = self.count + 1
		self.chain.append(block)

		string_object = json.dumps(block)
		block_string = string_object.encode()

		raw_hash = hashlib.sha256(block_string)
		hex_hash = raw_hash.hexdigest()
		self.chain.append(('Current hash: ', hex_hash))
		return block

block_chain = Block()
print(block_chain.chain)