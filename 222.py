# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-20

def get_shadow(time):
    hour, minute = time.split(":")
    time = int(hour)
    if minute == "30":
        time += 0.5

    if time < 6 or time == 12 or time >= 18:
        return "No shadow"

    dir = "east" if time > 12 else "west"
    diff = abs(12 - time)
    length = pow(diff, 3)

    return str(length) + "ft " + dir
