# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-11

def convert_words(s):
    lengths = []
    for word in s.split():
        lengths.append(str(len(word)))
    return " ".join(lengths)
