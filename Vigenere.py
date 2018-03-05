from CipherInterface import *

class Vigenere(CipherInterface):

    __slots__ = ['key', 'matrix']

    def __init__(self):
        self.key = ""
        self.matrix = []

        # Initialize alphabet matrix
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        for row in range(0, 25):
            curRow = []
            for i in range(0, 25):
                curRow.append(alphabet[(i+row) % 26])
            self.matrix.append(curRow)

        pass

    def setKey(self, key):
        self.key = ''.join(ch for ch in key if ch.isalpha()).lower()
        return True # Key initialized successfully

    def encrypt(self, pText):
        
        self.expandKey(pText)
        pText = ''.join(ch for ch in pText if ch.isalpha()).lower()
        cText = ""
        i = 0
        while i < len(pText):
            row = ord(self.key[i]) - ord('a')
            col = ord(pText[i]) - ord('a')
            cText += self.matrix[row][col]
            i += 1

        return cText

    def decrypt(self, cText):

        self.expandKey(cText)
        cText = ''.join(ch for ch in cText if ch.isalpha()).lower()
        pText = ""

        # Get the row, find which column the ciphertext letter is in,
        #  and then get the header for the column.
        i = 0
        while i < len(cText):
            row = ord(self.key[i]) - ord('a')
            col = self.matrix[row].index(cText[i])
            pText += chr(col + ord('a'))
            i += 1

        return pText
    
    # Repeat the key until it is the lenght of the input text
    def expandKey(self, text):
        if len(text) <= len(self.key):
            return

        expandedKey = ""
        keyIdx = 0
        i = 0
        while i < len(text):
            if keyIdx == len(self.key):
                keyIdx = 0

            expandedKey += self.key[keyIdx]
            keyIdx += 1
            i += 1
        
        self.key = expandedKey
