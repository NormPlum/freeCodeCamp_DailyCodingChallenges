# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-21

def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32

    if current_f < target_f:
        return "Heat: " + str(round(target_f - current_f, 1)) + " degrees Fahrenheit"
    elif current_f > target_f:
        return "Cool: " + str(round(current_f - target_f, 1)) + " degrees Fahrenheit"
    else:
        return "Hold"
