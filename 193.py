# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-19

def avalanche_risk(snow_depth, slope):
    if snow_depth == "Shallow" or slope == "Gentle":
        return "Safe"
    else:
        return "Risky"
