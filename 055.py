# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-04

def classification(temp):
    ranges = {
        30000: "O",
        10000: "B",
        7500: "A",
        6000: "F",
        5200: "G",
        3700: "K",
        0: "M",
    }

    for classification in ranges:
        if temp >= classification:
            return ranges[classification]
