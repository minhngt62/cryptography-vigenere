# CRYPTANALYSIS
from math import sqrt
import re

# Frequency
# {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75}
# ETAOIN

#Precondition: Capital letter
"""
Returns the letter that results from adding n to the input letter
--------------
Input:
letter: String. A char in the range [A-Z]
n: Int. Number that's going to be added to the letter
---------------
Output:
resultChar: Char
---------------
Example:
addToLetter("A", 4) = 'E'
"""
def addToLetter(letter, n): 
	positionInAlphabet = ord(letter) - 65
	newLetter = (positionInAlphabet + n) % 26
	return chr(newLetter + 65)

"""
Returns the euclidean distance from the frecuency of the letters ETAOIN to the frecuency of
these letters in Spanish
---------------
Input:
aeosFrecuencies: [Float]
Output:
Distance: Float
"""
def distanceToNormalFrenquencies(ETAOIN_frequencies):
	normalFrecuencies = [0.127, 0.0906, 0.0817, 0.0751, 0.0697, 0.0675]
	sum = 0
	for i in range(0, 6):
		sum += (normalFrecuencies[i] - ETAOIN_frequencies[i])**2
	return sqrt(sum)


"""
Returns the frecuencies of the input letters in a given text
---------------
Input:
letters: [String]. The letters to calculate the frecuency from
text: String
Output:
frecuencies: [Float]: The frecuencies of the letters in the input array
"""

def getNGrams(text, n): 
	regex = f".\x7B{n}\x7D"
	matches = re.findall(regex, text)
	nGrams = dict({})
	for match in matches:
		if match in nGrams:
			nGrams[match] = nGrams[match] + 1
		else:
			nGrams[match] = 1
	return sorted(nGrams.items(), key=lambda x: x[1], reverse=True)


def getLettersFrecuency(letters, text):
	criptogramLength = len(text)
	lettersDictionary = dict(getNGrams(text, 1)) #Dictionary [letter:repetitions].
	frecuencies = []
	for letter in letters:
		if not (letter in lettersDictionary):
			frecuencies.append(0)
		else:
			frecuencies.append(lettersDictionary[letter] / criptogramLength)
	return frecuencies


"""
Deciphers a message using the Vigenere Algorithm: M[i] = (C[i] - K[i] + 26) % 26
Input:
message: String
key: String
---------------
Output:
Deciphered message: String
---------------
Usage example:
decipher("FCGURWQOVDG", "DOS") = "COORDENADAS"
"""
def decipher(message, keyArray):
	messageLength = len(message)
	decipheredMessage = ""
	# keyArray = generate_key(key, messageLength)
	for i in range(0, messageLength):
		decipheredNumber = (ord(message[i]) - ord(keyArray[i]) + 26) % 26
		decipheredMessage += chr(decipheredNumber + 65)
	return decipheredMessage


"""
Divides a string into keyLength substrings
---------------
Input:
keyLength: Int
text: String
---------------
Output:
subcriptograms: [[String]]
"""
def getSubcriptograms(keyLength, text):
	textLength = len(text)
	return [text[i:textLength:keyLength] for i in range(0, keyLength)]

    
"""
Gets the key based on the keyLength, dividing the text on keyLength
substrings and applying to each one the AEOS procedure.
---------------
Input:
keyLength: Int
cipheredText: String
---------------
Output:
key: String
"""
def getKey(keyLength, cipheredText):
	criptograms = getSubcriptograms(keyLength, cipheredText)
	print(keyLength)
	possibleKey = []
	for criptogram in criptograms:
		#AEOS rule
		letters = getNGrams(criptogram, 1) #Ordered list of letters and their repetitions
		distances = []
		for i in range(0, 6): #We assume that AEOS will be among the 6 most common 
			possibleA = letters[i][0]
			possibleE = addToLetter(possibleA, 4)
			possibleO = addToLetter(possibleE, 10)
			possibleS = addToLetter(possibleO, 4)
			possibleAEOS = [possibleA, possibleE, possibleO, possibleS]
			frecuencies = getLettersFrecuency(possibleAEOS, criptogram)
			distances.append((possibleA, distanceToNormalFrenquencies(frecuencies)))
		sortedDistances = sorted(distances, key=lambda x: x[1])
		possibleKey.append(sortedDistances[0][0])
	return possibleKey



