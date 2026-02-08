# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-18

def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    to_fill = tank_size - fuel_level
    cost = to_fill * price_per_gallon
    return f"${cost:.2f}"
