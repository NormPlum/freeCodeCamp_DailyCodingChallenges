# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-20

def to_consonant_case(s):
    result = ""
    for char in s:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            result += char.lower()
        elif char == "-":
            result += "_"
        elif char.isalpha():
            result += char.upper()
        else:
            result += char
    return result
