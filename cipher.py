from Playfair import *
from RowTransposition import *
from Railfence import *
from Vigenere import *
from Caesar import *
import sys

cipher_name = None
key = None
method = None
input_file = None
output_file = None

def main():

    cipher = None

    # Determine which type of cipher
    if cipher_name == 'PLF':
        cipher = Playfair()

    elif cipher_name == 'RTS':
        print("Row Transposition")

    elif cipher_name == 'RFC':
        print("Railfence")

    elif cipher_name == 'VIG':
        print("Vigenere")

    elif cipher_name == 'CES':
        print("Ceasar")

    else:
        print("Not a valid cipher type! Please use:")
        print("\tPLF, RTS, RFC, VIG, or CES")
        return
    
    # Set the key
    cipher.setKey(key)

    # Attempt to read in the text the user wants to encrypt/decrypt
    inFile = None
    outFile = None
    
    try:
        inFile = open(input_file, "r")
    except FileNotFoundError:
        print("'", input_file, "' cannot be opened! Try a valid file")
        return

    # Prepare the output file
    outFile = open(output_file, 'w')

    # Perfrom the encryption/decryption
    if method == "ENC":
        plaintext = inFile.read()
        ciphertext = cipher.encrypt(plaintext)
        print(ciphertext)
        outFile.write(ciphertext)

    elif method == "DEC":
        ciphertext = inFile.read()

        plaintext = cipher.decrypt(ciphertext)
        outFile.write(plaintext)

    else:
        print("Incorrect method. Please enter 'ENC' or 'DEC'")
        return

    print("\nThank you for using this program :)")


if __name__ == "__main__":

    if len(sys.argv) == 6:
        cipher_name = sys.argv[1]
        key = sys.argv[2]
        method = sys.argv[3]
        input_file = sys.argv[4]
        output_file = sys.argv[5]

        main()
    else:
        print("Incorrect number of arguments")
        print("See format: \n\tpython3 <CIPHER NAME> <KEY> <ENC/DEC> <INPUTFILE> <OUTPUT FILE>")