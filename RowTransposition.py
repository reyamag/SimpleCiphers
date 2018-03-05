from CipherInterface import *

class RowTransposition(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        try:
            self.key = [int(c) for c in key.split()]
        except ValueError:
            print("Row Transposition cipher key must be a list of numbers!")
            print("\tExample: \"4 5 1 3 2\"")
            return False # Key not valid

        # Ensure that key contained a complete list from 1-n
        sorted = list(self.key)
        sorted.sort()
        for i in range(0, len(sorted)):
            if (i+1) != sorted[i]:
                print("Row Transposition cipher key must be a complete list of numbers from 1-n")
                return False # Key not valid

        return True  # Key initialized successfully

    def encrypt(self, pText):
        
        # Append 'xyz' until the grid is complete
        if len(pText) % len(self.key) != 0:
            ascii = ord('x')
            for _ in range(0, len(self.key) - len(pText) % len(self.key)):
                pText += chr(ascii)
                ascii += 1
                if ascii > ord('z'):
                    ascii = ord('x')

        # Strip non-alpha chars and cast to lower case
        pText = ''.join(ch for ch in pText if ch.isalpha()).lower()
        cText = ""
        cols = [[] for _ in range(0, len(self.key))]

        # Get plaintext into columns
        for i, c in enumerate(pText):
            cols[i % len(self.key)].append(c)

        # Rearrange columns according to key and append to ciphertext
        for col in self.key:
            cText += ''.join(cols[col-1])

        return cText

    def decrypt(self, cText):
        
        # Strip non-alpha chars and cast to lower case
        cText = ''.join(ch for ch in cText if ch.isalpha()).lower()
        pText = ""
        cols = [[] for _ in range(0, len(self.key))]
        orderedCols = []

        # Get ciphertext into cols
        i = 0
        colIdx = 0
        curDepth = 0
        maxDepth = len(cText) / len(self.key)
        while i < len(cText):
            if curDepth >= maxDepth:
                colIdx +=1
                curDepth = 0
            
            cols[colIdx].append(cText[i])
            curDepth += 1
            i += 1

        # Put columns back into order
        i = 0
        while i < len(self.key):
            for idx, col in enumerate(self.key):
                if col == i + 1:
                    orderedCols.append(cols[idx])
            i += 1
        
        # Get plaintext from sorted columns
        i = 0
        colIdx = 0
        while i < len(cText):
            pText += orderedCols[colIdx][0]
            orderedCols[colIdx].pop(0)
            
            colIdx = (colIdx + 1) % len(self.key)
            i += 1

        return pText
