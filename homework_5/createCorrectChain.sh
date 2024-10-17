#!/bin/bash

# Get the current working directory
current_dir=$(pwd)

# Creates a correct chain and stores it on disk
# Define the input variables here
poisonedChain=0  # 0 for correct blockchain, 1 for poisoned blockchain
# List of file paths separated by spaces
file_paths="$current_dir/data/transactions_one.txt $current_dir/data/transactions_two.txt" 

# Run the Python script and pass the inputs
python3 CreateBlockChain.py $poisonedChain $file_paths