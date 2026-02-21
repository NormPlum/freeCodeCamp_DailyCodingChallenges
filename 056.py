# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-05

def has_exoplanet(readings):
    values = []
    for reading in readings:
        if reading.isalpha():
            values.append(int(ord(reading) - 55))
        else:
            values.append(int(reading))

    average = sum(values) / len(values)

    for value in values:
        if value <= average * 0.8:
            return True

    return False
