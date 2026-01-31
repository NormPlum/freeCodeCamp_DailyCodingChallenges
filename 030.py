# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-09

def all_unique(s):
    characters = []
    for char in s:
        if char not in characters:
            characters.append(char)
        else:
            return False
    return True
