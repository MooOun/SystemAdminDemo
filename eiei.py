print('eieie')

def create_newblock(self,data):
        self.blockNo = len(self.blockchainList)+1
        self.nonce = random.randint(0,100)
        self.previous_hash=self.blockchainList[-1]['hash']
        self.timestamp=str(datetime.datetime.now())
        self.transaction=data
        self.hash=None

        self.hashblock()
        self.addToBlockkchain()