# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-14

def is_mirror_image(s1, s2):
    allowed = ["W", "T", "Y", "U", "I", "O", "H", "A", "X", "V", "M", "w", "o", "x", "v", "0", "8", "=", "+", ":", "|", "-", "_", "*", "^", "!", ".", " ", "[", "]", "{", "}", "<", ">", "b", "d", "p", "q", "(", ")"]

    mirrored = {
        "[": "]",
        "{": "}",
        "<": ">",
        "b": "d",
        "p": "q",
        "(": ")",
        "]": "[",
        "}": "{",
        ">": "<",
        "d": "b",
        "q": "p",
        ")": "(",
    }

    for char in (s1 + s2):
        if char not in allowed:
            return False

    reversed = list(s1[::-1])
    for i, char in enumerate(reversed):
        if char in mirrored:
            reversed[i] = mirrored[char]

    if "".join(reversed) == s2:
        return True
    else:
        return False
