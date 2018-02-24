from CipherInterface import *

class Caesar(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = int(key)

    def encrypt(self, pText, retainNonAlpha=False):

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
            # Shift by key value
            newLetterID = (letterID+self.key) % 26
            # Get the correct ASCII value by reapplying the offset
            cText += chr(newLetterID+ASCIIoffset)
        
        return cText

    def decrypt(self, cText, retainNonAlpha=False):
        
        pText = ""

        for letter in cText:
            if not letter.isalpha():
                if retainNonAlpha:
                    pText += letter
                continue
            
            # Determine the ASCII offset based on upper/lowercase
            ASCIIoffset = ord('A') if letter.isupper() else ord('a')
            
            # Get letter ID by factoring out the ASCII offset
            letterID = ord(letter)-ASCIIoffset
            # Shift by key value
            newLetterID = (letterID-self.key) % 26
            # Get the correct ASCII value by reapplying the offset
            pText += chr(newLetterID+ASCIIoffset)
        
        return pText