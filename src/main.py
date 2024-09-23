from MerkleTree import MerkleTree

# Prompting user for input
filename = input("Please enter the path to the file: ")


filename = '/Users/johncabrahams/Desktop/Projects/CSE-242-Resources/homework_3/transactions.txt'


merkle = MerkleTree()

merkle.fill(filename)

print(merkle.merkleToXML(merkle.tree))