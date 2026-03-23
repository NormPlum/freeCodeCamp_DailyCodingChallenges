# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-23

def has_no_repeats(s):
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return False
    return True
