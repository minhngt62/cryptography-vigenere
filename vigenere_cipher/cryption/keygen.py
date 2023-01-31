import random
import string

def generate_basekey(
    key_length: int
    ) -> str:
    return ''.join(random.choice(string.ascii_letters[26:]) for x in range(key_length))

def generate_key(length):
    baseKey = generate_basekey(length)
    baseKeyLength = len(baseKey)
    key = [baseKey[i % baseKeyLength] for i in range(0, length)]
    return key