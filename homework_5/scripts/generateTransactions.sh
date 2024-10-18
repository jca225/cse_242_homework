#!/bin/bash
# This scripts generates the transactions for our blockchain

# Get the current working directory 
current_dir=$(pwd)

# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")

# Generate transactional data and store it on disk
python3 $parent_dir/code/generateTransactions.py $parent_dir/transactions/transactions_one.txt $parent_dir/transactions/transactions_two.txt $parent_dir/transactions/transactions_three.txt