#!/bin/bash

# Get the current working directory
current_dir=$(pwd)

# Creates a correct chain and stores it on disk
# Define the input variables here
poisonedChain=0  # 0 for correct blockchain, 1 for poisoned blockchain
# List of file paths to store the transactions separated by spaces
destinations="$current_dir/transactions/transactions_one.txt $current_dir/transactions/transactions_two.txt $current_dir/transactions/transactions_three.txt"

destinationDir="$current_dir/blocks/"
# Run the Python script and pass the inputs
python3 code/chain/createBlockChain.py $poisonedChain $destinations $destinationDir