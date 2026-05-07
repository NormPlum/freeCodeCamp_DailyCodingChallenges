# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-07

def get_longest_substring(s):
    l = len(s)

    while(l > 0):
        l -= 1
        substrings = []

        for i in range(0, len(s) - (l - 1)):
            if s[i:l+i] in substrings:
                return s[i:l+i]
            else:
                substrings.append(s[i:l+i])
