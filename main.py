from vigenere_cipher.attacking import attack

from functools import reduce

'''
DEMO VIGENERE CIPHER
    1. plaintext, key --> VigenereCipher() --> ciphertext
    2. ciphertext --> Kasiski method --> key length
    3. ciphertext, key length --> cryptanalysis --> plaintext
'''

def main():
    file = 'test.txt'
    with open(file) as f:
        cyphertext = f.readlines()
    print("Cyphertext: ", cyphertext[0])
    
    print('---APPLYING KASISKI EXAMINATION---')
    attack(file)


if __name__ == '__main__':
    main()


