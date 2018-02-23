from CipherInterface import *

class Vigenere(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = key

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