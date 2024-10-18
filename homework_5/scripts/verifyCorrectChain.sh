# this script resets all of our data and creates a correct blockchain

# Reset transactions and blockchain
sh reset.sh
# Generate new transactions
sh generateTransactions.sh
# Create correct chain based on transactions
sh createCorrectChain.sh
# Verify
current_dir=$(pwd)
# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")
# Test
filesToTest="$parent_dir/blocks/blockchain.block.out"
python3 $parent_dir/code/verifier.py $filesToTest