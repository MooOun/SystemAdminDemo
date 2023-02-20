import datetime
from hashlib import sha256
import random
import tkinter as tk


class BlockChain:
    blockNo = 0
    nonce = 0
    transaction = None
    previous_hash = None
    hash = None
    timestamp = str(datetime.datetime.now())

    blockchainList = []

    def __init__(self):
        self.blockNo = 1
        self.nonce = random.randint(0, 100)
        self.previous_hash = "000000000000000"
        self.timestamp = str(datetime.datetime.now())

    def hashblock(self):
        newNonce = random.randint(1, 1000000000000)
        hashtext = str(self.blockNo) + str(newNonce) + str(self.transaction) + str(self.previous_hash) + self.timestamp
        blockhash = sha256(hashtext.encode()).hexdigest()

        self.hash = blockhash
        self.nonce = newNonce

    def addToBlockkchain(self):
        block = {
            'blockNo': self.blockNo,
            'nonce': self.nonce,
            'previous_hash': self.previous_hash,
            'transaction': self.transaction,
            'timestamp': self.timestamp,
            'hash': self.hash
        }
        self.blockchainList.append(block)

    def create_newblock(self, data):
        self.blockNo = len(self.blockchainList) + 1
        self.nonce = random.randint(0, 100)
        self.previous_hash = self.blockchainList[-1]['hash']
        self.timestamp = str(datetime.datetime.now())
        self.transaction = data
        self.hash = None

        self.hashblock()
        self.addToBlockkchain()


class BlockChainGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("BlockChain GUI")
        self.create_widgets()
        self.blockchain = BlockChain()

    def create_widgets(self):
        self.input_label = tk.Label(self.master, text="Enter transaction data:")
        self.input_label.pack(side="left")
        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack(side="left")
        self.input_entry.bind("<Return>", self.add_block)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(side="right")

        self.list_label = tk.Label(self.master, text="BlockChain List:")
        self.list_label.pack()
        self.list_box = tk.Listbox(self.master)
        self.list_box.pack()

    def add_block(self, event):
        data = self.input_entry.get()
        if data:
            self.blockchain.create_newblock(data)
            self.list_box.insert("end", self.format_block(self.blockchain.blockchainList[-1]))
            self.input_entry.delete(0, "end")

    def format_block(self, block):
        return f"Block ID: {block['blockNo']}, Nonce: {block['nonce']}, " \
               f"Transaction: {block['transaction']}, Previous Hash: {block['previous_hash']}, " \
               f"Hash: {block['hash']}, TimeStamp: {block['timestamp']}"

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockChainGUI(master=root)
    app.mainloop()
