# SimpleCiphers
Source code for 5 substitution &amp; transposition ciphers written with Python 3.6.

# Authors
Charles Bucher: charles.abucher@gmail.com <br>
Reyniel Maglian: rrmaglian@csu.fullerton.edu

# Instructions
To run, simply enter into the terminal:

***python3 cipher.py <CIPHER_NAME> \<KEY> <ENC/DEC> <INPUT_FILE> <OUTPUT_FILE>***

# Argument Descriptions

<CIPHER_NAME>:
  - PLF: Playfair
  - RTS: Row Transposition
  - RFC: Railfence
  - VIG: Vigenere
  - CES: Caser

\<KEY>:
  - The key that the encryption/decryption algorithm will use
  - Valid key values:
    - PLF: Any word or phrase
    - RTS: An inclusive, non-repeating list of space-separated numbers from 1-***n***, where ***n*** is less than or equal to the length of the cipher/plaintext
    - RFC: Any integer
    - VIG: Any word or phrase
    - CES: Any integer

<ENC/DEC>:
  - To decrypt, or encrypt, respectively
  
<INPUT_FILE>:
  - The file whose contents will be encrypted /decrypted.
  
<OUTPUT_FILE>:
  - The file that will be outputed with the encrypted/decrypted code.
