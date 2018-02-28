from Playfair import *
from RowTransposition import *
from Railfence import * # DONE
from Vigenere import *
from Caesar import * # DONE
import sys # Used for terminal args..

cipher_name = None
key = None
method = None
input_file = None
output_file = None

def main():
    print()
    cipher = None

    # Determine which type of cipher
    if cipher_name == 'PLF':
        cipher = Playfair()
    elif cipher_name == 'RTS':
        cipher = RowTransposition()
    elif cipher_name == 'RFC' or cipher_name == 'CES':
        try:
            shift_amt = int(key)
        except ValueError:
            print("ERR: Please enter a number as the key for a Caesar cipher!\n")
            return
        
        cipher = Railfence() if cipher_name == 'RFC' else Caesar()

    elif cipher_name == 'VIG':
        cipher = Vigenere()
    else:
        print("ERR: Not a valid cipher type! Please use:")
        print("\tPLF, RTS, RFC, VIG, or CES\n")
        return
    
    # Set the key
    if not cipher.setKey(key):
        print("ERR: Invalid key.\n")
        return

    inFile = None
    outFile = None
    
    # Attempt to read in the text the user wants to encrypt/decrypt
    try:
        inFile = open(input_file, "r")
    except FileNotFoundError:
        print("ERR: '", input_file, "' cannot be opened! Try a valid file\n")
        return

    # Prepare the output file
    outFile = open(output_file, 'w')
    # Perfrom the encryption/decryption
    if method == "ENC":
        # Read in the text to encrypt
        plaintext = inFile.read()
        # Encrypt
        ciphertext = cipher.encrypt(plaintext)
        # Write ciphertext to new file
        outFile.write(ciphertext)
        # Report success
        print("Encryption successfull!")

    elif method == "DEC":
        # Read in the text to decrypt
        ciphertext = inFile.read()
        # Decrypt
        plaintext = cipher.decrypt(ciphertext)
        # Write plaintext to new file
        outFile.write(plaintext)
        # Report success
        print("Decryption successfull!")

    else:
        print("ERR: Incorrect method. Please enter 'ENC' or 'DEC'\n")
        return

    print("Thank you for using this program.\n")


if __name__ == "__main__":

    if len(sys.argv) == 6:
        # Initialize variables
        cipher_name = sys.argv[1]
        key = sys.argv[2]
        method = sys.argv[3]
        input_file = sys.argv[4]
        output_file = sys.argv[5]

        main()
    else:
        print("ERR: Incorrect number of arguments")
        print("See format: \n\t$python3 cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>")
