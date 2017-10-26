import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#Genesis block
		self.new_block(previous_hash=1, proof= 100)
	
	#Create new block to add to chain
	def new_block(self, proof, previous_hash=None):
		
		block = {
			'index': len(self.chain) + 1
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}
	self.current_transactions = []
	self.chain.append(block)
	return block

	def proof_of_work(self, last_proof):
		"""
		Proof of Work algorithm:
		1. Find # p' so that hash(pp') contains 4 leading 0's where p is the previous p'.
		2. p is previous proof, p' is the new proof
		"""	
	
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof
	
	def valid_proof(last_proof, proof):
		"""
		Validates proof to see if it contains 4 leading 0s
		"""

		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"
		
	#Adds transaction to transaction list
	def new_transaction(self):
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount' : amount,
		})
		return self.last_block['index'] + 1

	#Hashes block with SHA-256
	@staticmethod
	def hash(block):	
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()	
		
	#Returns last block in chain
	@property
	def last_block(self):
		pass
		
