# Get current working directory
current_dir=$(pwd)

# Delete all the content in the transaction folder
rm -rf $current_dir/transactions/*

# Delete all the content in the blocks folder
rm -rf $current_dir/blocks/*