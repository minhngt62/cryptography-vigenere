import vigenere_cipher.attacking.cryptanalysis as crypt
import vigenere_cipher.attacking.frequency_analysis as fa
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
    key_length=30
    plaintext = "HELLOWORDHELLOWORDHELLOWORD"
    key = keygen.generate_key(key_length)
    vig_encryptor = vigenere.VigenereCipher(key, key_length)
    ciphertext = vig_encryptor.encrypt(plaintext)

    print("---PRIVATE PART---")
    print("\tKey length: ", key_length)
    print("\tActual key: ", key)
    print("\tPlain text: ", plaintext)
    
    ciphertext = ciphertext.upper()
    _, est_key_length = exam.estimateKeyLength(ciphertext)
    est_key = fa.restore_key(ciphertext, est_key_length)
    msg = crypt._decypher(ciphertext, est_key)

    print("Results")
    print("\tEstimated key length: ", est_key_length)
    print("\tEstimated key: ", est_key)
    print("\tResultant message: ", msg)


if __name__ == '__main__':
    main()


