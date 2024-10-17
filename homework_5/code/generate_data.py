import random
import sys

"""File for generating random transaction data"""
def generate_random_hex_string():
    # Define the hexadecimal alphabet for our account address
    hex_alphabet = '0123456789abcdef'
    
    # Generate a random string using random.choices
    random_hex_string = ''.join(random.choices(hex_alphabet, k=40))
    
    # Generate a random number between 0 and 100,000
    random_number = random.randint(0, 100000)


    return random_hex_string + " " + str(random_number) + "\0"
 

if __name__ == "__main__":

    file_paths = sys.argv[1:]  # First argument is the file path
    for file_path in file_paths:
        transactions = []
        # Generate a random number between 20 and 40 indicating the number of transactions
        numTransactions = random.randint(20, 40)
        # Generate random number of lines between
        with open(file_path, 'w') as file:
            # Loop through the number of transactions and write each the corresponding string to the file
            for _ in range(numTransactions):
                file.write(generate_random_hex_string() + '\n') 
            