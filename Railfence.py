from CipherInterface import *
from math import ceil

class Railfence(CipherInterface):

    # TERMINOLOGY: Rail = depth (col), Fence = length (row)

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = int(key)
        return True  # Key initialized successfully

    def encrypt(self, pText):

        # Strip non-alpha chars and cast to lower case
        pText = ''.join(ch for ch in pText if ch.isalpha()).lower()
        cText = ""
        rail = [[] for _ in range(self.key)]
        i = 0
        railIdx = 0

        # Convert the plaintext into fences
        while i < len(pText):

            # Reset rail index whenever rail depth is met
            if railIdx == self.key:
                railIdx = 0
                
            # Add next letter to correct fence in the rail.
            rail[railIdx].append(pText[i])
            
            i += 1
            railIdx += 1
        
        # In order, append each fence to the ciphertext
        for i in range(0, self.key):
            cText += ''.join(rail[i])

        return cText

    def decrypt(self, cText, retainNonAlpha=True):

        pText = ""
        
        numOfRails = ceil(len(cText) / self.key)
        rails = [[] for _ in range(numOfRails)]
        padBy1 =len(cText) % self.key
        i = 0

        while i < len(cText):
            for railIdx in range(0, numOfRails):
                if railIdx == numOfRails-1 and padBy1 == 0:
                    continue
                
                rails[railIdx].append(cText[i])
                i += 1

                if railIdx == numOfRails-1 and padBy1 != 0:
                    padBy1 -= 1

        for rail in rails:
            pText += ''.join(rail)

        return pText
