#!/bin/bash

# Get the current working directory
current_dir=$(pwd)

# Creates a poisonous chain and stores it on disk
# Define the input variables here
poisonedChain=1  # 0 for correct blockchain, 1 for poisoned blockchain
# List of paths to read
file_paths="$current_dir/transactions/transactions_one.txt $current_dir/transactions/transactions_two.txt $current_dir/transactions/transactions_three.txt"
# Destination file to store the block data
# Run the Python script and pass the inputs
destinationDir="$current_dir/blocks/"
python3 code/chain/createBlockChain.py $poisonedChain $file_paths $destinationDir