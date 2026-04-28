# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-27

def get_word_score(word):
    score = 0
    for char in word:
        value = ord(char.upper()) - 64
        score += value
    return score
