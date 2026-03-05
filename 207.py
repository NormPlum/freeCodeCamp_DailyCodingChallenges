# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-05

def smallest_gap(s):
    substrings = {}
    for i, char in enumerate(s):
        for j, char2 in enumerate(s[i+1:]):
            if char2 == char:
                substrings[i] = j
                break

    index = 0
    smallest = len(s)
    for i in substrings:
        if substrings[i] < smallest:
            index = i
            smallest = substrings[i]

    return s[index+1:index+1+smallest]
