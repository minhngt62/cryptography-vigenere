import random
import string

def generate_key(
    key_length: int
    ) -> str:
    return ''.join(random.choice(string.ascii_letters[26:]) for x in range(key_length))