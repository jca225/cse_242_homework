from hashlib import sha256
import math

def leafNode(leaf):
    """Constructs leaf node object"""
    if leaf == "":
        return {'type': 'leaf', 'hash': sha256(leaf.encode('utf-8')).hexdigest(), 'address': "", 'balance': ""} 
    return {'type': 'leaf', 'hash': sha256(str(leaf.split(' ')[0] + leaf.split(' ')[1]).encode('utf-8')).hexdigest(), 'address': leaf.split(' ')[0], 'balance': leaf.split(' ')[1]} 

def internalNode(left, right, hash=None):
    """Constructs internal node object"""
    if hash == None:
        return {'type': 'internal', 'left': left, 'right': right, 'hash': left['hash']}
    return {'type': 'internal', 'left': left, 'right': right, 'hash': sha256(hash.encode('utf-8')).hexdigest() }

class MerkleTree:
    def __init__(self):
        self.tree = None

    def fill(self, filename:str):
        # Each line is a leaf in our file
        leaves = []
        with open(filename) as file:
            for line in file:
                leaves.append(line[:-1])

        level = 0
        # Holds the hashed values in our file
        productions = [leafNode(leaf) for leaf in leaves]
        # Sort productions based on account address
        productions.sort(lambda leaf: leaf['address'])
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

    def merkleToXML(self, production, originalSpacing='', level=1):
        """This method takes as input dictionary, and outputs the tree in XML"""
        string = "<Node" + str(level) + ">" + '\n'
        if production['type'] != 'leaf':
            space = afterSpace = ""
            for i in range(level):
                space += '     '
            for i in range(level-1):
                afterSpace += '     '
            if production['left'] != None:
                string += space
                string += str(self.merkleToXML(production['left'], space, level=level+1)) 
                string += afterSpace + "</Node" + str(level) + ">" + '\n'
            if production['right'] != None:
                string += space
                string += str(self.merkleToXML(production['right'], space, level=level+1)) 
                string += afterSpace + "</Node" + str(level) + ">" + '\n'
        else:
            string += originalSpacing + '     ' + production['address'] + ' ' + production['balance'] + '\n'
            string += originalSpacing + "</Node" + str(level) + ">" + '\n'
        return string 

    def printMerkleTree(self):
        pass

