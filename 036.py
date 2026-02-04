# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-15

def adjust_thermostat(temp, target):
    if target > temp:
        return "heat"
    elif target < temp:
        return "cool"
    else:
        return "hold"
