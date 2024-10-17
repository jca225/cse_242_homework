from MerkleTree import MerkleTree
from blockchain import BlockChain

# Prompting user for input
filenames = input("Please enter the sequence of file paths (must be delimited by space): ").split(" ")

# Below is for testing purposes
# filenames = ['/Users/johncabrahams/Desktop/Projects/CSE-242-Resources/homeworks/homework_4/transactions.txt']

# create new blockchain
blockchain = BlockChain()
for filename in filenames:
    transactions = []
    with open(filename) as file:
            for line in file:
                transactions.append(line[:-1])
    merkleRootHash = MerkleTree().fill(filename)['hash']
    nonce = "0"
    while not blockchain.addBlock(merkleRootHash, transactions, nonce): 
         nonce = str(int(nonce) + 1)

    
newFilename = filenames[0].split(".txt")[0]
newFilename += ".block.out"
blockchain.printBlockChain(newFilename)
