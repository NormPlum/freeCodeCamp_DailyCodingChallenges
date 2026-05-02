# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-01

def group_anagrams(words):
    groups = []
    anagrams = []

    for word in words:
        chars = list(word)
        chars.sort()

        if chars in groups:
            i = groups.index(chars)
            anagrams[i].append(word)
        else:
            groups.append(chars)
            anagrams.append([word])

    return anagrams
