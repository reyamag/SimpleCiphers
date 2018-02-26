from CipherInterface import *

class Playfair(CipherInterface):

    __slots__ = ['key', 'keyRows', 'keyCols']

    def __init__(self):
        self.key = ""
        self.keyRows = [["" for _ in range(0,5)] for _ in range(0,5)]
        self.keyCols = [["" for _ in range(0,5)] for _ in range(0,5)]
        pass

    def setKey(self, key):

        key = key.lower()

        # Every letter that will be in the cipher
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        keyList = []

        while len(key) > 0:

            if not key[0].isalpha():
                key = key[1:]
                continue

            # If we already found this unique letter, remove it and move on.
            if key[0] in keyList:
                key = key[1:]
            # Special handling for i/j
            elif (key[0] == 'i' and 'j' in keyList) or \
                (key[0] == 'j' and 'i' in keyList):
                key = key[1:]
            else:
                # Add unique letter to the list!
                keyList.append(key[0])
        
        # Remove every letter from the alphabet that we already found
        for letter in keyList:
            if letter in alphabet:
                alphabet.remove(letter)
        # Add the rest of the alphabet letters!
        for letter in alphabet:
            # Special handling for i/j
            if letter == 'i' and 'j' in keyList or \
                letter == 'j' and 'i' in keyList:
                continue
            else:
                keyList.append(letter)

        self.key = ''.join(keyList)

        # Convert to rows & cols for easier access when encrypting/decrypting
        for row in range(0,5):
            for col in range(0,5):
                self.keyRows[col][row] = self.key[row + (col*5)]
                self.keyCols[row][col] = self.key[row + (col*5)]
    

    def encrypt(self, pText):
        # Perform encryption algorithm here...
        # ...
        # ...

        cText = "This is the encrypted string"

        return cText

    def decrypt(self, cText):
        # Perform decryption algorithm here...
        # ...
        # ...
        
        pText = "This is the decrypted string"

        return pText