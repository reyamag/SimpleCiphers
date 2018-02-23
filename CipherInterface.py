
class CipherInterface:

    def __init__(self):
        pass

    def setKey(key):
        raise NotImplementedError()
    
    def encrypt(self, plaintext):
        raise NotImplementedError()

    def decrypt(self, ciphertext):
        raise NotImplementedError()