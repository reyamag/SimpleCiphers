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

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

LICENSE:

Copyright 2017 Reyniel Maglian & Charles Bucher

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
