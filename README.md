# SimpleCiphers
Source code for 5 substitution &amp; transposition ciphers.

To run, simply enter into the terminal:

python3 cipher.py <CIPHER_NAME> <KEY> <ENC/DEC> <INPUT_FILE> <OUTPUT_FILE>

<CIPHER_NAME>:
  - PLF: Playfair
  - RTS: Row Transposition
  - RFC: Railfence
  - VIG: Vigenere
  - CES: Caser

<KEY>:
  - The key that the encryption/decryption algorithm will use

<ENC/DEC>:
  - To decrypt, or encrypt, respectively
  
<INPUT_FILE>:
  - The file whose contents will be encrypted /decrypted.
  
<OUTPUT_FILE>:
  - The file that will be outputed with the encrypted/decrypted code.
