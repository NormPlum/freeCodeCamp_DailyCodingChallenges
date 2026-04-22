# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-21

def get_odd_words(s):
    odd = []

    for word in s.split():
        if len(word) % 2 != 0:
            odd.append(word)

    return " ".join(odd)
