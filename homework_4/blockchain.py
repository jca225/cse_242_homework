import time
from hashlib import sha256

def header(previousBlockHeader, merkleRootHash, timestamp, difficultyTarget, nonce):
    return {"previous": previousBlockHeader, "merkleRootHash": merkleRootHash, "timestamp": timestamp, "difficultyTarget": difficultyTarget, "nonce": nonce}

def block(header, accounts):
    return {"header": header, "accounts": accounts}

def printBlock(block, displayAccounts=False, file=None):

    print("BEGIN BLOCK")
    print("BEGIN HEADER")
    for key in block["header"]:print(block["header"][key])
    print("END HEADER")
    if displayAccounts:
        for transaction in block["accounts"]: print(transaction)
    print("END BLOCK")

class BlockChain():

    def __init__(self):
        self.blocks = []
        self.difficultyTarget = int("00000000000000000000000000000000ffffffffffffffffffffffffffffffff", 16)

    def addBlock(self, merkleRootHash, transactions):
        timestamp = time.time()
        try:
            previousBlockHeader = sha256(self.blocks[-1]['merkleRootHash'].encode('utf-8')).hexdigest()
        except IndexError:
            previousBlockHeader = sha256(str(0).encode('utf-8')).hexdigest()
            
        # Random nonce
        nonce = "1e2b34084"
        
        headerInfo = header(previousBlockHeader, merkleRootHash, timestamp, self.difficultyTarget, nonce)
        newBlock = block(headerInfo, transactions)
        self.blocks.append(newBlock)

    def printBlockChain(self, filename):
        with open(filename, 'w') as f:
            for block in self.blocks:
                printBlock(block, True, f)
        