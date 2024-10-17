#!/bin/bash

# Test to see if a certian blockchain stored on disk is valid
file_path="file1.txt"  # File containing the poisoned or healthy blockchain

# Run the Python script and pass the inputs
python3 CreateBlockChain.py $file_path