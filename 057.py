# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-06

def send_message(route):
    time = 0
    speed = 300000

    for i, distance in enumerate(route):
        time += distance / speed
        if i != len(route) - 1:
            time += 0.5

    result = f"{time:.4f}"
    return float(result.strip("0"))
