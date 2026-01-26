# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-31

import random

def generate_hex(color):
    if color not in ["red", "green", "blue"]:
        return "Invalid color"

    dominant = hex(random.randint(200, 255))[2:]
    supplementary = hex(random.randint(0, 199))[2:]
    
    if color == "red":
        return dominant + supplementary + supplementary
    elif color == "green":
        return supplementary + dominant + supplementary
    elif color == "blue":
        return supplementary + supplementary + dominant
