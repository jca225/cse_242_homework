# This script resets all of our data and provides us with a clean slate

# Get the current working directory 
current_dir=$(pwd)

# Go to the parent directory of /scripts
parent_dir=$(dirname "$current_dir")

# Delete all the content in the transaction folder
rm -rf $parent_dir/transactions/*

# Delete all the content in the blocks folder
rm -rf $parent_dir/blocks/*