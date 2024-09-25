### Proof of Correctness


Our Merkle Tree relies on the `fill()` method to 
add values to it. Here we will prove its correctness:



Theorem: The function `fill()` will create a merkle tree that satisfied the following requirements:
1. Each node is a hash of its child
2. The tree is complete and balanced
3. If a leaf-node has no associated account and balance, then that node will have a hash of the empty string (denoted by $\epsilon$).

We will prove this method using induction:

Initial:
let $||\mathcal{l}||$ denote the number of leaves (i.e., the number of transactions)
if ${\lceil\log_2(||\mathcal{l}||)\rceil} \equiv \log_2(||\mathcal{l}||)$, then the bottom level is complete.
Our inner for loop loops through each of these leaves, and creates a corresponding parent node $p_i$. There is guaranteed to be $\frac{\log_2(||\mathcal{l}||)}{2}$ nodes on this level, each with the hash of two hashed and concatenated balances and accounts strings concatenated.
if ${\lceil\log_2(||\mathcal{l}||)\rceil} \neq \log_2(||\mathcal{l}||)$, then the bottom level is complete.
We increment the level, implying we have run the loop for the second time. On the second iteration, we find the desired number of nodes with the following equation:
$$2^{\lceil\log_2(||\mathcal{l}||)\rceil}$$
We find the difference in the number of nodes on the level versus the desired nodes, and create the corresponding nodes as leaves with the empty string hashed. 

Thus, level 1 has a complete number of nodes for all cases

Inductive step:
if level i is complete, then level i+1 will be complete. 
Inside the inner for loop, for every 2 nodes, we create a parent node $p_i$ that points to these two. Moreover, the hash of this node is the hash of the concatenated hashes for the child nodes. since the tree is complete, there will be exactly $2^{(n-(i + 1))}$ nodes, where $n$ is the height of the tree. This satisfied our completeness requirement.

Therefore, the method is correct by induction.