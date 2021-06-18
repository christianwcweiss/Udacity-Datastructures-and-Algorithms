import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = self.data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.tail_block = None
        self.block_dict = {}
        self.timestamps = set([])

    def add_block(self, timestamp, data):
        if (not timestamp or timestamp == "") and (not data or data == ""):
            print("Empty Block cannot be added!!")
            print("Block was not added")
            return
        if (timestamp in self.timestamps):
            print("Timestamp already added! Block couldn't be added")
            return
        if not self.tail_block:
            new_block = Block(timestamp, data, None)
            self.block_dict[new_block.hash] = new_block
            self.tail_block = new_block
        else:
            new_block = Block(timestamp, data, self.tail_block.hash)
            if new_block.hash in self.block_dict.keys():
                print("Collision detected!! The block was not added!")
                return
            self.block_dict[new_block.hash] = new_block
            self.tail_block.next = new_block
            self.tail_block = self.tail_block.next
        self.timestamps.add(timestamp)


block_chain = BlockChain()

#own test_cases
print("Test Case 1 - empty blockchain")
solution = None
output = block_chain.tail_block
print(output)
assert(output == None)
print("TestCase 1 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 2 - add a block")
solution = "8be9e6271e95f58c87b71836422c7a326d4f5d85019cd31264c568ea594922b6"
curr_timestamp = time.time()
s = "We are live on the blockchain!"
block_chain.add_block(curr_timestamp, s)
output = block_chain.tail_block.hash
print(output)
assert(output == solution)
print("TestCase 2 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 3 - added the same block again")
solution = None
curr_timestamp = time.time()
s = "We are live on the blockchain!"
block_chain.add_block(curr_timestamp, s)
output = block_chain.tail_block.previous_hash
print(output)
assert(output == solution)
print("TestCase 3 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 4 - added the same block again")
solution = "8be9e6271e95f58c87b71836422c7a326d4f5d85019cd31264c568ea594922b6"
curr_timestamp = time.time() + 1000 # +1000 to avoid same timestamps not being added from previous testcase
s = "Moon Moon Moon Lambo"
block_chain.add_block(curr_timestamp, s)
output = block_chain.tail_block.previous_hash
print(output)
assert(output == solution)
print("TestCase 4 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 5 - add empty block - None")
solution = "e073a4f9f4359f6dacebbeb42d1799b8ee62fa89721d3b42c56eeb677ff5e766"
curr_timestamp = None
s = None
block_chain.add_block(curr_timestamp, s)
output = block_chain.tail_block.hash
print(output)
assert(output == solution)
print("TestCase 5 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 6 - add empty block - empty strings")
solution = "e073a4f9f4359f6dacebbeb42d1799b8ee62fa89721d3b42c56eeb677ff5e766"
curr_timestamp = ""
s = ""
block_chain.add_block(curr_timestamp, s)
output = block_chain.tail_block.hash
print(output)
assert(output == solution)
print("TestCase 6 passed! - Given output {0}; Expected output {1}".format(output, solution))
print("---------------------------")
print("Test Case 7 - add empty block - empty strings")
solution = "e073a4f9f4359f6dacebbeb42d1799b8ee62fa89721d3b42c56eeb677ff5e766"
curr_timestamp = time.time() + 2000 # +2000 to avoid same timestamps not being added from previous testcase
s1 = "1"
s2 = "2"
block_chain.add_block(curr_timestamp, s1)
block_chain.add_block(curr_timestamp, s2)
output = block_chain.tail_block.previous_hash
print(output)
assert(output == solution)
print("TestCase 7 passed! - Given output {0}; Expected output {1}".format(output, solution))