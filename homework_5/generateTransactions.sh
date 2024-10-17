#!/bin/bash
current_dir=$(pwd)
# Generate transactional data and store it on disk
python3 code/generate_data.py $current_dir/transactions/transactions_one.txt $current_dir/transactions/transactions_two.txt $current_dir/transactions/transactions_three.txt