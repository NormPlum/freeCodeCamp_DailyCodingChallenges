# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-15

def jbelmu(text):
    output = ""
    
    for word in text.split():
        output += jumble_word(word) + " "
    
    return output.rstrip()


# Jumble the letters of a word.
def jumble_word(word):
    if len(word) <= 2:
        return word
    
    jumbled = ""
    letters = list(word)

    first = letters.pop(0)
    last = letters.pop()
    letters.sort()
    
    jumbled += first
    for l in letters:
        jumbled += l
    jumbled += last

    return jumbled
