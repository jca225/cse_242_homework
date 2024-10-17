from hashlib import sha256
import math

def leafNode(leaf):
    """Constructs leaf node object"""
    if leaf == "":
        return {'type': 'leaf', 'hash': sha256(leaf.encode('utf-8')).hexdigest(), 'address': "", 'balance': ""} 
    return {'type': 'leaf', 'hash': sha256(str(leaf.split(' ')).encode('utf-8')).hexdigest(), 'address': leaf.split(' ')[0], 'balance': leaf.split(' ')[1]} 

def internalNode(left, right, hash=None):
    """Constructs internal node object"""
    if hash == None:
        return {'type': 'internal', 'left': left, 'right': right, 'hash': left['hash']}
    return {'type': 'internal', 'left': left, 'right': right, 'hash': sha256(hash.encode('utf-8')).hexdigest() }

class MerkleTree:
    """Lightweight class meant to scope the creation and search of a merkle tree. Also supports printing and searching."""
    def __init__(self):
        self.tree = None

    def fill(self, ledger:list):
        """Creates our merkle tree based on the ledger."""
        leaves = ledger
        level = 0
        # Holds the hashed values in our file
        productions = [leafNode(leaf) for leaf in leaves]
        # Sort productions based on account address
        productions.sort(key=lambda leaf: leaf['address'])
        while len(productions) != 1:
            new_productions = []

            # Add 'padding' to the nodes on the secont to last level to maintain the complete and balanced invarianrt
            if level==1:
                numberOfNodes = 2**math.ceil(math.log(len(productions), 2))
                nodesToConstruct = numberOfNodes - len(productions)
                for i in range(nodesToConstruct):
                    productions.append(leafNode(""))

            for i in range(0, len(productions), 2):
                left_node = productions[i]
                try:
                    right_node = productions[i+1]
                    new_hash = left_node['hash'] + right_node['hash']
                    node = internalNode(left_node, right_node, new_hash)
                    new_productions.append(node)

                # I.e., we have an odd number of leaves
                except IndexError:
                    # Maintain invariant: every level but the bottom one must be complete
                    if level==0:
                        node = internalNode(left_node, None)
                    else:
                        raise IndexError("Expected even number of nodes at level: " + str(level))
                    new_productions.append(node)
            level+=1
            productions = new_productions
        self.tree = productions[0]
        return productions[0]


    def printMerkleTree(self, currentNode=None, indent=0):
        """
            Print a merkle tree utilizing post-order traversal.
            Source: https://stackoverflow.com/questions/13484943/print-a-binary-tree-in-a-pretty-way
        """
        # If we are at the beginning of the tree set the current node to the root node
        if not currentNode: currentNode=self.tree
        try:
            self.printMerkleTree(currentNode['left'], indent+4)
            self.printMerkleTree(currentNode['right'], indent+4)
        except KeyError:
            print("Address: " + currentNode['address'] + ". Balance: " + currentNode['balance'])
        print(currentNode['hash'])


    def searchTree(self,account):
        """Takes as input an account and finds the path associated with that account, including siblings"""
        hashedAccount = sha256(str(account.split(' ')).encode('utf-8')).hexdigest()
        pathList = []
        self.auxSearchTree(self.tree, hashedAccount, pathList)
        return pathList

    
    def auxSearchTree(self, node, hashedAccount, pathList):
        """This is an auxiliary method that allows us to search the leaves of the tree and find the 
           corresponding path"""
        # Base case: We are at a leaf
        if node['type'] == "leaf":
            # If we have found the hashed account append it to the list of accounts and exit
            if node['hash'] == hashedAccount:
                pathList.append(node['hash'])
                return
        # Recursive step: We are at a node with a child
        else:
            # Search the left tree
            self.auxSearchTree(node['left'], hashedAccount, pathList)
            # NOTE: "The account exists in the substree denoted by node['left']"" == "len(pathList) > 0"
            if len(pathList) != 0:
                # Add the current node's hash to the list of paths
                pathList.append(node['right']['hash'], node['hash'])
            # Otherwise, we search the right tree. In this way our algorithm is left-biased
            else:
                self.auxSearchTree(node['right'], hashedAccount, pathList)
                if len(pathList) != 0:
                    pathList.append(node['left']['hash'], node['hash'])
                

