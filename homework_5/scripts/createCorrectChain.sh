#!/bin/bash
# This script creates a correct blockchain

# reset filesystem
sh reset.sh 

# Generate transactions
sh generateTransactions.sh

# Get the current working directory 
current_dir=$(pwd)

# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")

# Creates a correct chain and stores it on disk
poisonedChain=0  # 0 for correct blockchain, 1 for poisoned blockchain

# List of file paths to store the transactions separated by spaces
destinations="$parent_dir/transactions/transactions_one.txt $parent_dir/transactions/transactions_two.txt $parent_dir/transactions/transactions_three.txt"

# Where to store the blockchain
destinationDir="$parent_dir/blocks/"

# Run the Python script from the parent directory and pass the inputs
python3 "$parent_dir/code/chain/createBlockChain.py" $poisonedChain $destinations $destinationDir