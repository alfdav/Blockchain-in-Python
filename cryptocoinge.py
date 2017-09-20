#Learning how to make my own Blockchain in python.
#This is our block structure.
import hashlib as hasher
class Block:
	def __init__ (self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block (self):
		sha = hasher.sha256()
		sha.update(str(self.index) +
				str(self.timestamp) +
				str(self.data) +
				str(self.previous_hash))

		return sha.hexdigest()

#Now we create our genesis block

import datetime as date

def create_gen_block():
	#Mannually construct a block with index zero (0) and arbitratry previous hash
	return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
	dis_index = last_block.index + 1
	dis_timestamp = date.datetime.now()
	dis_data = "Le block " + str(dis_index)
	dis_hash = last_block.hash
	return Block (dis_index, dis_timestamp, dis_data, dis_hash)


#This will create the blockchain and add the gen block

blockchain = [create_gen_block()]
previous_block = blockchain[0]

#How many blocks should we add to the chain
#after the genesis block

num_of_blocks_to_add = 50

#Add blocks to the chain
for i in range (0, num_of_blocks_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

	#Yay Print now.

	print "Block #{} has been added to the blockchain!".format(block_to_add.index)
	print "Hash: {}\n".format(block_to_add.hash)