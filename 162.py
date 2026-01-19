# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-19

def compare_energy(calories_burned, watt_hours_used):
    calorie = 4184
    watt_hour = 3600

    calories = calories_burned * calorie
    watt_hours = watt_hours_used * watt_hour

    if calories > watt_hours:
        return "Workout"
    elif watt_hours > calories:
        return "Devices"
    else:
        return "Equal"
