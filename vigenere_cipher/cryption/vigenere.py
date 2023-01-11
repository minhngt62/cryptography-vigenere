from typing import List, Optional
from . import keygen as K

class VigenereCipher:
    def __init__(
        self,  
        key: Optional[str] = None,
        key_length: Optional[int] = None
        ):
        if key is None:
            assert type(key_length) == int
            key = K.generate_key(key_length) # randomize a key with
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for i in range(len(plaintext)):
            ch = (ord(plaintext[i]) + ord(self.key[i % len(self.key)])) % 26
            ch += ord("A")
            ciphertext = ciphertext + chr(ch)
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        for i in range(len(ciphertext)):
            ch = (ord(ciphertext[i]) - ord(self.key[i % len(self.key)])) % 26
            ch += ord("A")
            plaintext = plaintext + chr(ch)
        return plaintext
