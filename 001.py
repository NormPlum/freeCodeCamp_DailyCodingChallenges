# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-11

def is_balanced(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    left_vowels = 0
    right_vowels = 0

    halfway = int(len(s) / 2)
    left = s[:halfway]
    right = s[-halfway:]

    for i in range(halfway):
        if left[i].lower() in vowels:
            left_vowels += 1
        if right[i].lower() in vowels:
            right_vowels += 1

    return left_vowels == right_vowels
