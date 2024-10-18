# this script resets all of our data and creates a poisonous blockchain

# Reset transactions and blockchain
sh reset.sh
# Generate new transactions
sh generateTransactions.sh
# Create poisonous chain based on transactions
sh createPoisonousChain.sh
# Verify
current_dir=$(pwd)
# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")
# Test
filesToTest="$parent_dir/blocks/blockchainpoisonedMerkle.block.out $parent_dir/blocks/blockchainpoisonedTransaction.block.out"
python3 $parent_dir/code/verifier.py $filesToTest