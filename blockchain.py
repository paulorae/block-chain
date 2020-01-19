import datetime
import hashlib

#BlockClass

class Block:

	block_number	= 0
	data			= None
	next			= None
	hash 			= None
	nonce			= 0
	previous_hash	= 0x0
	timestammp 		= datetime.datetime.now()

	def __init__(self, data):
		self.data	= data

	def hash(self):
		h = hashlib.sha256()
		h.update(
				str(self.nonce).encode("utf-8") +
				str(self.data).encode("utf-8") +
				str(self.previous_hash).encode("utf-8") +
				str(self.timestammp).encode("utf-8") +
				str(self.block_number).encode("utf-8")
				)

		return h.hexdigest()

	def __str__(self):
		return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.block_number) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

#BlockChain Class

class BlockChain:

	difficulty = 12
	MaxNonce = 2**32
	target = 2 ** (256-difficulty)

	block = Block("BlockOne")
	head = block

	def add_block(self, block):
	
		block.previous_hash = self.block.hash()
		block.block_number = self.block.block_number + 1

		self.block.next = block
		self.block = self.block.next

	def mine_block(self, block):
		for x in range(self.MaxNonce):
			if int(block.hash(), 16) <= self.target:
				self.add_block(block)
				break
			else:
				block.nonce += 1

	# @classmethod
	# def change_difficulty(cls, value):
		
	# 	max_limit = 50
	# 	if value > max_limit:
	# 		cls.difficulty = int(cls.difficulty + max_limit)
	# 	else:
	# 		cls.difficulty = int(cls.difficulty + value)
	# 	return cls.difficulty
memo = '''
    ---------Block Chain Concept Practice-----
    #                                        #
    #        Forgive for being newbie        #
    #        Trying to Learn Everyday        #
    #                                        #
    ------------------------------------------
    '''

print(memo)
blockchain = BlockChain()
block_quantity = int(input("How many Blocks"))
# block_difficulty = blockchain.change_difficulty(int(input("enter")))

for i in range(block_quantity):
	blockchain.mine_block(Block("Block" + str(i +1)))

while blockchain.head != None:
	print(blockchain.head)
	blockchain.head = blockchain.head.next