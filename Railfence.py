from CipherInterface import *

class Railfence(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = int(key)
        return True  # Key initialized successfully

    def encrypt(self, pText):

        # Strip non-alpha chars and cast to lower case
        pText = ''.join(ch for ch in pText if ch.isalnum()).lower()
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
        rail = [[] for _ in range(self.key)]
        i = 0
        railIdx = 0
        fenceIdx = 0
        baseLen = int(len(cText) / self.key) # The base fence length
        padBy1 = len(cText) % self.key # The number of fences with length+1
        
        # Convert the ciphertext into fences
        while i < len(cText):
            # Add letter to the right rail.
            rail[railIdx].append(cText[i])
            i += 1

            # Keep track of where we are on the fence so we know
            # when we need to move to the next one.
            fenceIdx += 1
            if fenceIdx == baseLen + padBy1:
                railIdx += 1
                fenceIdx = 0
                # There are a limited number of fences that will be padded by 1.
                if padBy1 != 0:
                    padBy1 -= 1

        # Now that our fences are separated, retrieve the plaintext.
        counter = 0
        for j in range(baseLen+1): # The fence index
            for i in range(self.key): # The rail index
                if counter == len(cText):
                    return pText
                pText += rail[i][j]
                counter += 1

        return pText
