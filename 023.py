# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-02

def rgb_to_hex(rgb):
    hexadecimal = "#"

    values = rgb[4:-1].split(", ")
    r, g, b = values

    for color in [r, g, b]:
        hex_color = hex(int(color))[2:]
        if len(hex_color) < 2:
            hex_color = "0" + hex_color
        hexadecimal += hex_color

    return hexadecimal
