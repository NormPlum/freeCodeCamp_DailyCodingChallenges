# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-02

def get_deepest_brackets(s):
    open_brackets = 0
    current_word = ""
    deepest = 0
    result = ""

    for char in s:
        if char in ["[", "{", "("]:
            open_brackets += 1
            current_word = ""
        elif char in ["]", "}", ")"]:
            if open_brackets > deepest:
                deepest = open_brackets
                result = current_word
            open_brackets -= 1
            current_word = ""
        else:
            current_word += char

    return result
