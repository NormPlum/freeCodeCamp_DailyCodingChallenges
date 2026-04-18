# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-17

def decode(message):
    key = "VLHCGMDLNHVLHCGMDLNHVLHCGMDLNHVLHCGMDLNH"
    unicode_diff = 64
    letters = 26
    decoded = ""
    i = 0

    for char in message:
        if char.isalpha():
            key_num = ord(key[i]) - unicode_diff
            char_num = ord(char) - unicode_diff

            diff = char_num - key_num
            if diff < 1:
                diff = letters + diff

            letter = chr(diff + unicode_diff)
            i += 1
        else:
            letter = char

        decoded += letter

    return decoded
