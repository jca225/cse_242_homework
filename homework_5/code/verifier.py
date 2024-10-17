from chain.MerkleTree import MerkleTree
from chain.blockchain import BlockChain
import sys

class Verifier:
    """Class verifies our blockchain. Takes as input the serialized blockchain stored on disk"""

    def parse_file(self, filepath):
        """Takes as input the file containing the serialized blockchain and returns a local copy of it. Most of this is 
           just reading in a file of a specific type and instantiating a local copy of the blockchain"""
        # Stores parsed blocks
        parsed_blocks = []
        # Open the file where the serialized blockchain is stored
        with open(filepath, 'r') as f:
            # stores each serialized block
            serializedBlocks = []
            # Stores local blocks
            self.localChain = []
            # Loop through each line in the file
            for line in f:
                # Detect the start and end of a block
                if line == "BEGIN BLOCK":
                    # Append a new array indicating a new block
                    serializedBlocks.append([])
                    continue
                # Don't add anything to the block if we are at the end
                elif line == "END BLOCK":
                    continue
                # Add file info to the block
                else:
                    serializedBlocks[-1].append(line)
            
            # Now we loop through each serialzed block and
            # store them locally
            for block in serializedBlocks:
                # Define accounts
                accounts = []
                # Define line index
                lineIndex = 0
                # Loop through all values. the `while` loop lets us 
                # increment lineIndex within the loop easily, which is 
                # necessary for parsing the header.
                while lineIndex < range(len(block)):
                    # We have an exact format for our header
                    if line[lineIndex] == "BEGIN HEADER":
                        # Define all of our values
                        previousBlockHash = line[lineIndex+1]
                        merkleHash = line[lineIndex+2]
                        timestamp = int(line[lineIndex+3])
                        difficultyTarget = int(line[lineIndex+4])
                        nonce = int(line[lineIndex+5])
                        # Assert the next line is the end of the header
                        assert(line[lineIndex+6] == "END HEADER")
                    # Append the line to the list of accounts
                    else:
                        accounts.append(line[lineIndex])
                # Create merkle tree based on our account information
                merkleTreeInstance = MerkleTree()
                merkleTreeInstance.fill(accounts)
                # Construct local block
                localBlock = self._constructLocalBlock(previousBlockHash, merkleHash, timestamp, difficultyTarget, nonce, accounts, merkleTreeInstance)
                # Append it to the local chain
                self.localChain.append(localBlock)

    def _constructlocalBlock(self,previousBlockHash, merkleHash, timestamp, difficultyTarget, nonce, accounts, merkleTree):
        """Constructs a local representation of a block"""
        return {"previousBlockHash":previousBlockHash, "merkleHash":merkleHash,"timestamp":timestamp,"difficultyTarget":difficultyTarget,"nonce":nonce,"accounts":accounts,"merkleTree":merkleTree}

    # NOTE: The following methods are part of the assignment. All of the code above is just scaffolding
    def verifyBlock(self, block):
        """Takes a block as input and returns a boolean indicating if it is valid. 
           We calculate a merkle root for ourselves and ensure they match"""
        return block["merkleTreeInstance"].tree['hash'] == block["merkleHash"]
    
    def verifyChain(self, blockchain):
        """Check correctness of hashes of previous blocks"""
        for block in blockchain:
            if not self.verifyBlock(block):
                return False
        return True

    def balance(self, targetAddress:str, blockchain: BlockChain):
        """Takes an address string and a blockchain and returns the balance of that address, including a proof of membership."""
        # Start at the most recent block
        for i in range(len(blockchain.blocks)-1, 0, -1):
            block = blockchain.blocks[i]
            # Search for the account in each block
            for accountIdx in range(len(block["accounts"])):
                if block["accounts"][accountIdx].split(" ")[0] == targetAddress:
                    # return proof of membership and balance
                    proofOfMem = self.proofOfMembership(block["accounts"][accountIdx], block["merkleTree"])
                    accountBalance = block["accounts"][accountIdx].split(" ")[1]
                    return proofOfMem, accountBalance
        # We break out of the loop when the address is found on the chain
        # Getting to the end of the loop implies the address was not found.
        return False
    
    def proofOfMembership(self, account, merkleTreeInstance):
        """Conduct proof of membership. Check to see if an account is on chain, and get the path to the account. """
        return merkleTreeInstance.searchTree(account)
    


if __name__ == "main":
    filenames = sys.argv[1:]
    # Instantiate verifier
    verifier = Verifier()
    for filename in filenames:
        print("validating file " + filename + ".")
        # Create local blockchain stored on verifier class
        verifier.parse_file(filename)
        # validate blockchain
        print("Validating the chain...")
        # check for certain address
        print("Assert and address exists on chain")

"""
Players:
Full node
Light client
graders invoke membership function and test it


Somebody has to have the instance of the merkle tree. 
Each block has a bunch of transactions, merkle root, merkle tree
Here is a well-known place to find the root of the transactions

Blockchain contains proof of membership
Block being linked up among all the blocks
merkle tree on chain for us.

They can create their own input and use your code to create a new blockchain
Ask a membership question.
Look at what comes out from your code, the blockchain you created

Take any arbitrary data on disk meant to emulate a blockchain as input and validate it

Create sh file for creating this


You already have a blockchain.
Creating blocks in blockchain -> input transactions, done
Now, Buy cup of coffee -> send me a transaction, i want to check if this is in a certain place to make sure it is valid
Looking for a proof that in the blockchain this transaction being spent to me is in the merkle tree
Asking the full node to provide a proof of membership
"""