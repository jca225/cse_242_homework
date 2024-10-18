#!/bin/bash
current_dir=$(pwd)

# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")

#filesToTest="$current_dir/blocks/blockchainpoisonedMerkle.block.out $current_dir/blocks/blockchainpoisonedTransaction.block.out"
filesToTest="$parent_dir/blocks/blockchain.block.out"
python3 $parent_dir/code/verifier.py $filesToTest