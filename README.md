### Proof of Correctness


Our Merkle Tree relies on the `fill()` method to 
add values to it. Here we will prove its correctness:

Initial:
On the first iteration, we loop through all the leaves. For every 2 leaves, we create a corresponding internal node and save it in an auxiliary list. These internal nodes point to two leaves. This auxiliary list becomes our main one, and the size of the list decreases by a 
factor of 2.
If there are an odd number of leaves, 
        

Inductive:

Final: