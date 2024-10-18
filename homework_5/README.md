## Architecture
+ `generateTransactions.py` generates random transactions following the form dictated by Professor Hank Korth. These transactions are stored in `/transactions`
+ `blockchain.py` scopes all of our methods pertaining to the creation of a blockchain. You can think of it as an auxiliary class for creating a blockchain.
+ `createBlockchain.py` instantiates the class declared in `blockchain.py` to create a blockchain and **store it on disk**. There are two classes: One that creates a correct blockchain and one that creates an incorrect blockchain. These blockchains are then stored on disk and given the appropriate names. We refer to the incorrect blockchain as poisonous. 
+ `verifier.py` takes these blockchains stored on disk created by `createBlockchain.py`, and verifies their validity. This file is meant to emulate a full node. 

