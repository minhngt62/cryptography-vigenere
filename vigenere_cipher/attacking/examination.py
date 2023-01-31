# KASISKI METHOD
import re
from functools import reduce



def gcd(x:int, y:int) -> int:
    while(y):
        x, y = y, x % y
    return abs(x)

def getNGrams(text, n): 
    """
    Returns an ordered list of touples representing, from greatest to lowest, all
    the nGrams found in the text and their number of repetitions
    ---------------
    Input:
    text: String. The text to analyze
    n: Int. The length of the n-grams
    ---------------
    Output:
    nGrams: [(String, Int)]
    ---------------
    Example:
    getNGrams("ABCDEFABC", 3) = [("ABC", 2), ("DEF", 1)]
    """
    regex = f".\x7B{n}\x7D"
    matches = re.findall(regex, text)
    nGrams = dict({})
    for match in matches:
        if match in nGrams:
            nGrams[match] = nGrams[match] + 1
        else:
            nGrams[match] = 1
    return sorted(nGrams.items(), key=lambda x: x[1], reverse=True)

def getNGramPositions(nGram, text):
    
    """
    Returns all the indexes where a certain nGram ends in a given text
    ---------------
    Input:
    nGram: String. Regular expression of the nGram
    text: String. The text in which to look for ocurrences
    ---------------
    Output:
    Positions: [Int]
    """
    matches = re.finditer(nGram, text)
    positions = []
    for match in matches:
        positions.append(match.end(0))
    return positions

def estimateKeyLength(cipheredText):
    assert len(cipheredText) > 20
    def estimateKeyLength(cipheredText, maxSamples):
        tetraGrams = getNGrams(cipheredText, 4)
        triGrams = getNGrams(cipheredText, 3)
        positions = []
        i = 0
        j = 0
        while len(positions) < maxSamples: 
            if tetraGrams[i][1] >= 2:
                positions.append(getNGramPositions(tetraGrams[i][0], cipheredText))
                i+=1
            elif triGrams[i][1] >= 2:
                positions.append(getNGramPositions(triGrams[j][0], cipheredText))
                j+=1
            else:
                break
        differences = []
        for pos in positions:
            differences += [y - x for x, y in zip(pos, pos[1:])]
        print(differences)
        return reduce(gcd, differences)

    keyLength = 1
    maxSamples = 6
    while (keyLength == 1 and maxSamples > 1):
        maxSamples -= 1
        keyLength = estimateKeyLength(cipheredText, maxSamples)
    return cipheredText, keyLength

if __name__ == "__main__":
    """
    plain text: INTELLIPAAT
    key: RINTELLIPAA
    """
    cipheredText = "ZVGXVGXPWTXDPAAFRTZVGX" #PWTXPATZVGXPWTXPAT"
    print(len(cipheredText))
    # print(find_key_length(cipheredText, SEQ_LEN, MAX_KEY_LEN))
    print(estimateKeyLength(cipheredText=cipheredText))
