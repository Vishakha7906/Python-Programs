from string import ascii_lowercase
ALPHABET = set(ascii_lowercase)
def is_pangram(string):
#A pangram  is a sentence using every letter of the alphabet at least once. 
    return ALPHABET.issubset(string.lower())
