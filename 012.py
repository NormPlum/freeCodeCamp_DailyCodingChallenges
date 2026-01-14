# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-22

def decode(message, shift):
    output = ""
    for char in message:
        if char.isalpha():
            char = shift_letter(char, shift)
        output += char
    return output


def shift_letter(l, n):
    uppercase = False
    a = "a"
    z = "z"
  
    old = ord(l)
    if old <= ord("Z"):
        uppercase = True
    if uppercase:
        a = "A"
        z = "Z"

    new = old - n
    if new > ord(z):
        new = new - ord(z) + ord(a) - 1
    elif new < ord(a):
        new = new - ord(a) + ord(z) + 1

    return chr(new)
