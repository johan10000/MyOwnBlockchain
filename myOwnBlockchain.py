import hashlib # To use sha256 algorithm

def hashGenerator(data): # To get hash of data
  result = hashlib.sha256(data.encode()) # To hash data
  # sha 256 doesn't gives us result in hexadecimal form
  return result.hexdigest() # To return the hashed data in 64 hexadecimal form

class Block: # Let's create our block
  def __init__(self, data, hash, prevHash):
    self.data = data
    self.hash = hash
    self.prevHash = prevHash
    # This block has only 3 fields: transaction data, current block's hash, previous block's hash

class BlockChain: # Let's start creating our blockchain
  def __init__(self):
    hashLast = hashGenerator('genLast') # Hash of block previous to genesis block
    hashStart = hashGenerator('genHash') # Hash of genesis block
    
    genesis = Block('genData', hashStart, hashLast) # Creating genesis block
    self.chain = [genesis]

  def addBlock(self, data): # To add a block in blockchain
      prevHash = self.chain[-1].hash # Get hash of previous block to form a chain
      hash = hashGenerator(data + prevHash) # To generate hash of current block
      block = Block(data, hash, prevHash) # To create current block
      self.chain = self.chain + [block] # To add the current block to the blockchain

bc = BlockChain() # Genesis block gets created, 0th block
bc.addBlock('1') # Add first block
bc.addBlock('2') # Add second block
bc.addBlock('3') # Add third block

for block in bc.chain:
  print(block.__dict__)
