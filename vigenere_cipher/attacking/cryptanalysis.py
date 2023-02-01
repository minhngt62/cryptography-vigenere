import sys
sys.path.append('/Users/lggvu/Projects/HUST/Crypto/cryptography-vigenere/vigenere_cipher/attacking')
import processing
import frequency_analysis as fa
import string


def _decypher(cyphertext, key):
    letters = string.ascii_uppercase
    shifts = [letters.index(letter) for letter in key]
    blocks = processing.get_blocks(text=cyphertext,size=len(key))
    cols = processing.get_columns(blocks)
    decyphered_blocks = processing.to_blocks([fa.shift(col, shift) for col, shift in zip(cols, shifts)])
    decyphered = ''.join(decyphered_blocks)
    return decyphered