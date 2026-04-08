# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-07

def palindrome_locator(s):
    half = int(len(s) / 2)
    first = s[:half]
    second = s[-half:]

    for i in range(len(first)):
        if first[i] != second[-(i+1)]:
            return "none"

    if len(s) / 2 == half:
        return s[half-1:][:2]
    else:
        return s[half:][0]
