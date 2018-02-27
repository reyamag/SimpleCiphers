from CipherInterface import *

class Playfair(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        # Interpret key as a 5x5 matrix
        self.key = [["" for _ in range(0,5)] for _ in range(0,5)]
        pass


    def setKey(self, key):

        # Strip non-alpha chars and cast to lower case
        key = ''.join(ch for ch in key if ch.isalnum()).lower()

        # Every letter that must be in the cipher
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        keyList = []

        while len(key) > 0:
            # If we already found this unique letter, remove it and move on.
            if key[0] in keyList:
                key = key[1:]
            # Special handling for i/j
            elif (key[0] == 'i' and 'j' in keyList) or (key[0] == 'j' and 'i' in keyList):
                key = key[1:]
            else:
                # Add unique letter to the list!
                keyList.append(key[0])
                # Remove this letter from the alphabet since we found it already
                alphabet.remove(key[0])

        # Finally, add every letter we didn't find
        for letter in alphabet:
            # Special handling for i/j
            if (letter == 'i' and 'j' in keyList) or (letter == 'j' and 'i' in keyList):
                continue
            else:
                keyList.append(letter)

        key = ''.join(keyList) # Convert list to string

        # Convert string to our key matrix for easier access when encrypting/decrypting
        for row in range(0,5):
            for col in range(0,5):
                self.key[row][col] = key[col + (row * 5)]
    

    def encrypt(self, pText):
        # Strip non-alpha chars and cast to lower case
        pText = ''.join(ch for ch in pText if ch.isalnum()).lower()
        pTextPaired = ""
        cText = ""
        
        # Convert input to be correctly formatted by pairs
        i = 0
        while i < len(pText):
            # Check if on last character
            if i+1 != len(pText):
                # Check if same character
                if pText[i] == pText[i+1]:
                    # Split the pair by adding an 'x'
                    pTextPaired += pText[i] + 'x'
                    i += 1
                else:
                    # Append the pair itself
                    pTextPaired += pText[i:i+2]
                    i += 2
            else:
                # We need pairs of two, add 'x' to last character
                pTextPaired += pText[i] + 'x'
                i += 1
        
        # Get ciphertext
        i = 0
        while i <len(pTextPaired):
            # Since we already formatted the text into pairs of two, we do not need to check bounds
            pair = pTextPaired[i:i+2]

            # The location of the first pair within the key matrix.
            first = (0, 0)
            second = (0, 0)

            # The location of the encrypted pair
            newFirst = (0, 0)
            newSecond = (0, 0)

            # Get the location of the pair based on col/rows
            for row in range(0,5):
                if pair[0] in self.key[row]:
                    first = (row, self.key[row].index(pair[0]))
                if pair[1] in self.key[row]:
                    second = (row, self.key[row].index(pair[1]))

            # If pair is in same row/col, simply shift down/right
            if first[0] == second[0]:
                newFirst = (first[0], (first[1]+1) % 5)
                newSecond = (second[0], (second[1]+1) % 5)
            elif first[1] == second[1]:
                newFirst = ((first[0]+1) % 5, first[1])
                newSecond = ((second[0]+1) % 5, second[1])
            else:
                # Otherwise, swap cols
                newFirst = (first[0], second[1])
                newSecond = (second[0], first[1])

            # Update the ciphertext
            cText += self.key[newFirst[0]][newFirst[1]]+self.key[newSecond[0]][newSecond[1]]

            i += 2

        return cText


    def decrypt(self, cText):
        print(cText)
        pText = ""

        # Get ciphertext
        i = 0
        while i <len(cText):
            # Since we already formatted the text into pairs of two, we do not need to check bounds
            pair = cText[i:i+2]
            # The location of the first pair within the key matrix.
            first = (0, 0)
            second = (0, 0)

            # The location of the encrypted pair
            newFirst = (0, 0)
            newSecond = (0, 0)

            # Get the location of the pair based on col/rows
            for row in range(0,5):
                if pair[0] in self.key[row]:
                    first = (row, self.key[row].index(pair[0]))
                if pair[1] in self.key[row]:
                    second = (row, self.key[row].index(pair[1]))

            # If pair is in same row/col, simply shift up/left
            if first[0] == second[0]:
                newFirst = (first[0], (first[1]-1) % 5)
                newSecond = (second[0], (second[1]-1) % 5)
            elif first[1] == second[1]:
                newFirst = ((first[0]-1) % 5, first[1])
                newSecond = ((second[0]-1) % 5, second[1])
            else:
                # Otherwise, swap cols
                newFirst = (first[0], second[1])
                newSecond = (second[0], first[1])

            # Update the ciphertext
            pText += self.key[newFirst[0]][newFirst[1]]+self.key[newSecond[0]][newSecond[1]]

            i += 2

        return pText
