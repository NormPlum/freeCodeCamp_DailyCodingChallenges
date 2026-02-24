# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-08

import math

def goldilocks_zone(mass):
    luminosity = math.pow(mass, 3.5)
    zone_start = math.sqrt(luminosity) * 0.95
    zone_end = math.sqrt(luminosity) * 1.37
    return [round(zone_start, 2), round(zone_end, 2)]
