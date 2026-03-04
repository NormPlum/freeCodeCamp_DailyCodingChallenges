# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-04

def card_values(cards):
    values = []

    for card in cards:
        value = card[:-1]
        if value == "A":
            value = 1
        elif value.isalpha():
            value = 10
        values.append(int(value))

    return values
