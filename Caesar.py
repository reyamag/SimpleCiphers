from CipherInterface import *

class Caesar(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = int(key)
        return True  # Key initialized successfully

    def encrypt(self, pText, retainNonAlpha=True):

        cText = ""

        for letter in pText:
            if not letter.isalpha():
                if retainNonAlpha:
                    cText += letter
                continue
            
            # Determine the ASCII offset based on upper/lowercase
            ASCIIoffset = ord('A') if letter.isupper() else ord('a')
            
            # Get letter ID by factoring out the ASCII offset
            letterID = ord(letter)-ASCIIoffset
            
            # Shift right by key value
            newLetterID = (letterID+self.key) % 26
            
            # Get the correct ASCII value by reapplying the offset
            cText += chr(newLetterID+ASCIIoffset)
        
        return cText

    def decrypt(self, cText, retainNonAlpha=True):
        
        pText = ""

        # Same logic as encrypt()
        for letter in cText:
            if not letter.isalpha():
                if retainNonAlpha:
                    pText += letter
                continue
            
            ASCIIoffset = ord('A') if letter.isupper() else ord('a')
            letterID = ord(letter)-ASCIIoffset
            # Shift left by key value
            newLetterID = (letterID-self.key) % 26
            pText += chr(newLetterID+ASCIIoffset)
        
        return pText
