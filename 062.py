# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-11

def hex_to_decimal(hex):
    decimal = 0
    reverse = hex[::-1]

    for i, char in enumerate(reverse):
        if char.isdecimal():
            value = int(char)
        else:
            value = ord(char) - 55
        decimal += value * pow(16, i)

    return decimal
