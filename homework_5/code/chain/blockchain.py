import time
from hashlib import sha256

    
class BlockChain():
    """Lightweight class meant to emulate a blockchain. Functionality includes adding and printing a block.
       Difficulty target is static and left on chain."""

    def __init__(self):
        # Holds the list of blocks
        self._blocks = []
        # Sets the difficutly target
        self._difficultyTarget = int("00000000000000000000000000000000ffffffffffffffffffffffffffffffff", 16)

    def addBlock(self, merkleRootHash, transactions, nonce):
        """Add a block to the chain"""
        # Get the time the block was added
        timestamp = time.time()
        # try block implicitly checks to see if we are adding the first block on chain
        try:
            # Hash previous merkle root hash
            previousBlockHeader = sha256(self._blocks[-1]['merkleRootHash'].encode('utf-8')).hexdigest()
        except:
            # Hash "0" and set that as the previous block header
            previousBlockHeader = sha256(str(0).encode('utf-8')).hexdigest()
        
        # This is where the user tries adding a block with a nonce that is less than or equal to the difficulty target
        if int(sha256((merkleRootHash + nonce).encode('utf-8')).hexdigest(),16) > self._difficultyTarget:
            return False
        # Instantiate header with python dictionary (meant to emulate a struct in C)
        headerInfo = self._header(previousBlockHeader, merkleRootHash, timestamp, self._difficultyTarget, nonce)
        # Instantiate block 
        newBlock = self._block(headerInfo, transactions)
        # Append to list of blocks
        self._blocks.append(newBlock)
        return True

    def printBlockChain(self, filename):
        """Loop through elements and print blockchain to specific file"""
        with open(filename, 'w') as f:
            for block in self._blocks:
                self._printBlock(block, True, f)
    
    def _header(self, previousBlockHeader, merkleRootHash, timestamp, difficultyTarget, nonce):
        """Constructs header"""
        return {"previous": previousBlockHeader, "merkleRootHash": merkleRootHash, "timestamp": timestamp, "difficultyTarget": difficultyTarget, "nonce": nonce}

    def _block(self, header, accounts):
        """Constructs block"""
        return {"header": header, "accounts": accounts}

    def _printBlock(self, block, displayAccounts=False, file=None):
        """Print block"""
        # Print block
        print("BEGIN BLOCK", file=file)
        # Print header
        print("BEGIN HEADER", file=file)
        # Loop through the attributes of our header and print them
        for key in block["header"]:
            print(block["header"][key], file=file)
        # Print end header
        print("END HEADER", file=file)
        if displayAccounts:
            for transaction in block["accounts"]: print(transaction, file=file)
        print("END BLOCK", file=file)
        print("\n", file=file)

