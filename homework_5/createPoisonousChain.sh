#!/bin/bash

# Creates a poisonous chain and stores it on disk
# Define the input variables here
poisonedChain=1  # 0 for correct blockchain, 1 for poisoned blockchain
file_paths="file1.txt file2.txt file3.txt"  # List of file paths separated by spaces

# Run the Python script and pass the inputs
python3 CreateBlockChain.py $poisonedChain $file_paths