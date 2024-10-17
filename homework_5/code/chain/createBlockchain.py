from MerkleTree import MerkleTree
from blockchain import BlockChain
from hashlib import sha256
import random
import sys


class CreateBlockChain:
    """Abstraction for blockchain creation. This class creates an entire Blockchain and outputs it to disk. 
       This is meant to emulate downloading a blockchain to look at it"""
    def __init__(self, filenames, destinationDir):
        """Read transactions in and put them onto disk as blockchain"""
        self.destinationDir = destinationDir
        # Create new blockchain. 
        blockchain = BlockChain()
        # Loop through files and add block to blockchain for each file
        for filename in filenames:
            # Holds transactions
            transactions = []
            # Open file
            with open(filename) as file:
                for line in file:
                    transactions.append(line[:-2])
            # Create merkle root hash
            merkleRootHash = MerkleTree().fill(transactions)['hash']
            # Try adding the block to the blockchain
            nonce = "0"
            while not blockchain.addBlock(merkleRootHash, transactions, nonce): 
                nonce = str(int(nonce) + 1)

        # Format filename to output block to
        newFilename = self.destinationDir + "blockchain"
        newFilename += ".block.out"
        # Print blockchain
        blockchain.printBlockChain(newFilename)    



class CreateIncorrectBlockChain:
    """Abstraction for "blockchain poison." We create a normal blockchain then edit some of the fields."""
    def __init__(self, destinationDir):
        self.destinationDir = destinationDir
    def poisonMerkleHash(self, filenames):
        """Read transactions in and poison them"""
        # Create new blockchain. 
        blockchain = BlockChain()
        # Loop through files and add block to blockchain for each file
        for filename in filenames:
            # Holds transactions
            transactions = []
            # Open file
            with open(filename) as file:
                for line in file:
                    transactions.append(line[:-2])
            # Create merkle root hash
            merkleRootHash = MerkleTree().fill(transactions)['hash']
            # Poison merkle root hash by hashing it again
            poisonedMerkleRootHash = sha256(str(merkleRootHash).encode('utf-8')).hexdigest()
            # Try adding the block to the blockchain
            nonce = "0"
            while not blockchain.addBlock(poisonedMerkleRootHash, transactions, nonce): 
                nonce = str(int(nonce) + 1)

        # Format filename to output block to
        newFilename = self.destinationDir + "blockchain"
        newFilename += "poisonedMerkle.block.out"
        # Print poisoned blockchain
        blockchain.printBlockChain(newFilename)    
    
    def poisonTransactions(self, filenames):
        """Read transactions in and poison them"""
        # Create new blockchain. 
        blockchain = BlockChain()
        # Loop through files and add block to blockchain for each file
        for filename in filenames:
            # Holds transactions
            transactions = []
            # Open file
            with open(filename) as file:
                for line in file:
                    transactions.append(line[:-2])
            # Create merkle root hash
            merkleRootHash = MerkleTree().fill(transactions)['hash']
            for i in range(len(transactions)):
                # Hex alphabet
                hex_alphabet = '0123456789abcdef'
    
                # Generate a poisonedAddress using random.choices of length 40
                poisonedAddress = ''.join(random.choices(hex_alphabet, k=40))
                
                # Get the balance associated with the transaction
                balance = transactions[i].split(" ")[1]
                # Poison the trnasaction by adding it to the list
                transactions[i] = " ".join([poisonedAddress, balance])
            # Try adding the block to the blockchain
            nonce = "0"
            while not blockchain.addBlock(merkleRootHash, transactions, nonce): 
                nonce = str(int(nonce) + 1)

        # Format filename to output block to
        newFilename = self.destinationDir + "blockchain"
        newFilename += "poisonedTransaction.block.out"
        # Print poisoned blockchain
        blockchain.printBlockChain(newFilename)    


# If the file is run directly create a blockchain of a certain type for testing purposes
if __name__ == "__main__":
    # Get inputs from command line arguments
    poisonedChain = int(sys.argv[1])  # First argument: poisonedChain
    filenames = sys.argv[2:-1]  # All other arguments except for the last: filenames
    directory = sys.argv[-1]  # Last argument: location to store the files

    # If the user chose to create a poisoned chain
    if poisonedChain:
        incorrectBlockChainCreator = CreateIncorrectBlockChain(directory)
        # We create a blockchain with a poisoned merkle hash and push it to disk
        incorrectBlockChainCreator.poisonMerkleHash(filenames)
        # We create a blockchain with a poisoned transaction list and push it to disk
        incorrectBlockChainCreator.poisonTransactions(filenames)
        
    else:
        # Create a healthy chain and push it to disk
        blockChainCreator = CreateBlockChain(filenames, directory)