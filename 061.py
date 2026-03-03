# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-10

def launch_fuel(payload):
    weight = payload
    current_fuel = 0

    needed_fuel = weight / 5
    additional_fuel = needed_fuel - current_fuel
    while additional_fuel > 1:
        weight += additional_fuel
        current_fuel += additional_fuel

        needed_fuel = weight / 5
        additional_fuel = needed_fuel - current_fuel

    return round(needed_fuel, 1)
