# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-03

def is_pangram(sentence, letters):
    sentence = sentence.lower()

    for char in sentence:
        if char.isalpha():
            if char not in letters:
                return False
    
    for letter in letters:
        if letter not in sentence:
            return False

    return True
