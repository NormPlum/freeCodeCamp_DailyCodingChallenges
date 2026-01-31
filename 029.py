# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-08

def build_acronym(s):
    ignored = ["a", "for", "an", "and", "by", "of"]
    acronym = ""

    words = s.split()
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in ignored:
            acronym += word[0].upper()

    return acronym
