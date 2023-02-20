import datetime
from hashlib import sha256
import random


class BlockChain:
    blockNo=0
    nonce=0
    transaction=None
    previous_hash=None
    hash=None
    timestamp=str(datetime.datetime.now())
    
    blockchainList=[]

    def __init__(self):
        self.blockNo=1
        self.nonce=random.randint(0,100)
        self.previous_hash="000000000000000"
        self.timestamp=str(datetime.datetime.now())
        
 # สร้างฟังก์ชั่น Hashblock       
    # def hashblock(self):
    #     newNonce=random.randint(1,1000000000000)
    #     hashtext=str(self.blockNo)+str(newNonce)+str(self.transaction)+str(self.previous_hash)+self.timestamp
    #     blockhash=sha256(hashtext.encode()).hexdigest()
    #     self.hash=blockhash
    #     self.nonce=newNonce



   # สร้างฟังก์ชั่น Hashblock 2      
    # def hashblock(self):
    #     newNonce=random.randint(1,1000000000000)
    #     hashtext=str(self.blockNo)+str(newNonce)+str(self.transaction)+str(self.previous_hash)+self.timestamp
    #     blockhash=sha256(hashtext.encode()).hexdigest()
    #     self.hash=blockhash
    #     self.nonce=newNonce 

    def addToBlockkchain(self):
        block={
            'blockNo':self.blockNo,
            'nonce':self.nonce,
            'previous_hash':self.previous_hash,
            'transaction':self.transaction,
            'timestamp':self.timestamp,
            'hash':self.hash
        }
        self.blockchainList.append(block)
    
    def create_newblock(self,data):
        self.blockNo = len(self.blockchainList)+1
        self.nonce = random.randint(0,100)
        self.previous_hash=self.blockchainList[-1]['hash']
        self.timestamp=str(datetime.datetime.now())
        self.transaction=data
        self.hash=None

        self.hashblock()
        self.addToBlockkchain()

    def hashblock(self):
        nonce_limit = 100000000000
        zeroes = 4

        for rand_nonce in range(nonce_limit):
            basetext = str(self.blockNo)+str(self.transaction)+str(self.previous_hash)+self.timestamp+str(rand_nonce)
            hashblock = sha256(basetext.encode()).hexdigest()
            if hashblock.startswith('0'*zeroes):
                print(f"found hash with Nonce {rand_nonce}")
                self.nonce = rand_nonce
                self.hash = hashblock
                return hashblock
        raise BaseException(f"Couldn't find Correct hash after trying {nonce_limit} time")



print('Build BlockChain')

#เรียกใช้งานฟังก์ชั่น 
block=BlockChain()
block.hashblock()
block.addToBlockkchain()

#สร้างBlockChainใหม่
block.create_newblock("block 2")
block.create_newblock("block 3")
block.create_newblock("block 4")
block.create_newblock("block 5")


#แสดงผล Loop ในบล็อคเชน
for block in block.blockchainList:
    print()
    print("Block ID : ", block['blockNo'])
    print("Nonce : ", block['nonce'])
    print("Transaction : ", block['transaction'])
    print("Previous Hash : ", block['previous_hash'])
    print("Hash : ", block['hash'])
    print("TimeStamp : ", block['timestamp'])
  


