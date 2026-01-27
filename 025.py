# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-04

def repeat_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    new_string = ""

    for char in s:
        new_string += char
        if char.lower() in vowels:
            for i in range(count):
                new_string += char.lower()
            count += 1

    return new_string
