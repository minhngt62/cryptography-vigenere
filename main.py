from vigenere_cipher.attacking import attack
from vigenere_cipher.cryption import VigenereCipher

from functools import reduce

'''
DEMO VIGENERE CIPHER
    1. plaintext, key --> VigenereCipher() --> ciphertext
    2. ciphertext --> Kasiski method --> key length
    3. ciphertext, key length --> cryptanalysis --> plaintext
'''

def main():
    # load the test data
    file = 'test.txt'
    print(">> [SYSTEM] Loading test text")
    with open(file) as f:
        text = f.readlines()
    print("Plaintext:", text[1])
    print("Key:", text[2])
    print("Ciphertext:", text[0])

    # vigenere cipher
    print('>> [SYSTEM] Applying Vigenere Cipher......')
    cypher = VigenereCipher(key=text[2].strip())
    
    ciphertext = cypher.encrypt(text[1].strip())
    assert ciphertext == text[0].strip()
    print(">> [ENCODER] Encryption assertions passed")

    decrypt_text = cypher.decrypt(ciphertext)
    assert decrypt_text == text[1].strip()
    print(">> [DECODER] Decryption assertions passed")
    
    # kasiski exam
    print('\n>> [SYSTEM] Start attacking with Kasiski examination......')
    attack(file)


if __name__ == '__main__':
    main()


