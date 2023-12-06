import hashlib
import json
from time import time

class Block(object):

	def __init__():
		self.chain = []
		self.new_transactions = []
		self.count = 0
		self.new_block(previous_hash = 'No previous hash since this is the genesis block.')

	def new_block(self, previous_hash = None):
		block = {
		'Block Number' : self.count,
		'Timestamp' : time(),
		'Transactions' : self.new_transactions or 'No previous transactions since this is the genesis block.',
		'Gasfee' : 0.1,
		'previous_hash' : previous_hash or self.hash(self.chain[-1]),
		}

		self.new_transactions = []
		self.count += 1

		#Adding block into chain variable
		self.chain.append(block)
		return block

	def last_block(self):
		return self.chain[-1]

	def transaction(self, sender, recipient, amount):
		    sender_encoder = hashlib.sha256(sender.encode())
		    sender_hash = sender_encoder.hexdigest()

		    recipient_encoder = hashlib.sha256(recipient.encode())
		    recipient_hash = recipient_encoder.hexdigest()

		    transaction_data = {
	    	'Sender' : sender_hash,
	    	'Recipient' : recipient_hash,
	    	'Amount' : amount,
	    	}

	    	self.new_transactions.append(transaction_data)
	    	return self.last_block
    	

    def hash(self, block):
	    	string_object = json.dumps(block)
	    	block_string = string_object.encode()

	    	raw_hash = hashlib.sha256(block_string)
	    	hex_hash = raw_hash.hexdigest()
	    	self.chain.append(('Current hash: ', hex_hash))
	    	return hex_hash

blockchain = Block()
transactionOne = blockchain.transaction('Jack', 'Johna', '0.02 ETH')
transactionTwo = blockchain.transaction('Pablo', 'Pedro', '0.162 ETH' )
transactionThree = blockchain.transaction('Kev', 'Marie', '0.046 ETH')

blockchain.new_block()
print(blockchain.chain)

#python ClassC242Two.py