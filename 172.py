# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-29

def separate_letters_and_numbers(s):
    result = ""

    for i, char in enumerate(s):
        if i > 0:
            if char.isalpha() and not previous_was_letter:
                result += "-"
            elif not char.isalpha() and previous_was_letter:
                result += "-"

        previous_was_letter = char.isalpha()
        result += char

    return result
