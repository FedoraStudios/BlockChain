import hashlib
import json
from time import time

class Block(object):
	def __init__(self):
		self.chain = []
		self.new_transactions = []
		self.count = 0
		self.new_block(previous_hash = 'No previous hash since this is the first block', proof = 100)
		self.proof = 100

	def new_block(self, proof, previous_hash = None):
		block = {
		'block number' : self.count,
		'timestamp' : time(),
		'transactions' : self.new_transactions or 'No transaction, genisis block',
		'gasfee' : 0.1,
		'nonce' : proof,
		'previous_hash' : previous_hash or self.hash(self.chain[-1]),
		}

		self.new_transactions = []
		self.count = self.count +1
		self.chain.append(block)

		return block

	def last_block(self):
		return self.chain[-1]

	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof_condition = False
		while check_proof_condition is False:
			compare_proof = new_proof**2 - previous_proof**2
			string_compare_proof = str(compare_proof).encode()
			encode_proof = hashlib.sha256(string_compare_proof)
			hash_proof = encode_proof.hexdigest()
			print('Obtaining proof of work: ', hash_proof)

			if hash_proof[:4] == '0000':
				check_proof_condition = True

			else:
				new_proof = new_proof +1

		return new_proof
    
    #def hash(self, block):
    #	string_object = json.dumps(block, sort_keys = True)
    #	block_string = string_object.encode()
    #	raw_hash = hashlib.sha256(block_string)
    #	hex_hash = raw_hash.hexdigest()
    #	block['Current hash'] = hex_hash
    #	return hex_hash

blockchain = Block()
transactionOne = blockchain.transaction('Pedro', 'Jason', '0.16 ETH')
transactionTwo = blockchain.transaction('Juan', 'Mason', '0.24 ETH')
transactionThree = blockchain.transaction('John', 'Madison', '0.5 ETH')

previous_block = blockchain.last_block()
print('Our previous block: ', previous_block)

previous_proof = previous_block['nonce']
print('Previous block proof: ', previous_proof)

proof = blockchain.proof_of_work(previous_proof)
print('Found proof of work at: ', proof)

previous_hash = blockchain.hash(previous_block)
print('Previous block hash: ', previous_hash)

block = blockchain.new_block(proof, previous_hash)
print('Data of blockchain: ', blockchain.chain)