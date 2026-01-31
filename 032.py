# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-11

def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
