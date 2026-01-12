# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-16

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    string1 = list(str1.lower())
    string1.sort()
    string2 = list(str2.lower())
    string2.sort()

    return string1 == string2
