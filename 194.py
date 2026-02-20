# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-20

def is_valid_trick(trick_name):
    first_words = [
        "Misty",
        "Ghost",
        "Thunder",
        "Solar",
        "Sky",
        "Phantom",
        "Frozen",
        "Polar",
    ]
    second_words = [
        "Twister",
        "Icequake",
        "Avalanche",
        "Vortex",
        "Snowstorm",
        "Frostbite",
        "Blizzard",
        "Shadow",
    ]

    words = trick_name.split()
    if words[0] in first_words and words[1] in second_words:
        return True
    else:
        return False
