from CipherInterface import *

class Casar(CipherInterface):

    __slots__ = ['key']

    def __init__(self):
        self.key = ""
        pass

    def setKey(self, key):
        self.key = key

    def encrypt(self, pText):
        cText = "This is the encrypted string"

        return cText

    def decrypt(self, cText):
        pText = "This is the decrypted string"

        return pText