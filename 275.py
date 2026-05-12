# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-12

def get_frequency(s):
    characters = {}

    for char in s:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters
