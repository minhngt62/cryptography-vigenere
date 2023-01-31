import vigenere_cipher.attacking.cryptanalysis as crypt
import vigenere_cipher.attacking.examination as exam
import vigenere_cipher.cryption.keygen as keygen
import vigenere_cipher.cryption.vigenere as vigenere

from functools import reduce

'''
DEMO VIGENERE CIPHER
    1. plaintext, key --> VigenereCipher() --> ciphertext
    2. ciphertext --> Kasiski method --> key length
    3. ciphertext, key length --> cryptanalysis --> plaintext
'''

def main():
    key_length=10
    plaintext = "HELLOMODAFAKA"
    key = keygen.generate_key(key_length)
    vig_encryptor = vigenere.VigenereCipher(key, key_length)
    ciphertext = vig_encryptor.encrypt(plaintext)

    print("---PRIVATE PART---")
    print("\tKey length: ", key_length)
    print("\tActual key: ", key)
    print("\tPlain text: ", plaintext)
    
    ciphertext = ciphertext.upper()
    _, estimated_key_length = exam.estimateKeyLength(ciphertext)
    key_letters = crypt.getKey(estimated_key_length, ciphertext)

    if key_letters == []:
        print("Unable to decrypt message")
        exit(1)
    
    es_key = reduce(lambda x,y: x+y, key_letters)
    message = crypt.decipher(ciphertext)

    print("Results")
    print("\tEstimated key length: ", estimated_key_length)
    print("\tEstimated key letters: ", key_letters)
    print("\tEstimated key: ", es_key)
    print("\tResultant message: ", message)


if __name__ == '__main__':
    main()


