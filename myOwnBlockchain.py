import hashlib # To use sha256 algorithm

def hashGenerator(data):
  result = hashlib.sha256(data.encode()) # To hash data
  return result.hexdigest() # To return the hashed data in hexadecimal form

class Block:
  def __init__(self, data, hash, prevHash):
    self.data = data
    self.hash = hash
    self.prevHash = prevHash

class BlockChain:
  def __init__(self):
    hashLast = hashGenerator('genLast')
    hashStart = hashGenerator('genHash')
    
    genesis = Block('genData', hashStart, hashLast) # Creating genesis block
    self.chain = [genesis]

  def addBlock(self, data):
      prevHash = self.chain[-1].hash
      hash = hashGenerator(data + prevHash)
      block = Block(data, hash, prevHash)
      self.chain = self.chain + [block]

bc = BlockChain()
bc.addBlock('1')
bc.addBlock('2')
bc.addBlock('3')

for block in bc.chain:
  print(block.__dict__)
