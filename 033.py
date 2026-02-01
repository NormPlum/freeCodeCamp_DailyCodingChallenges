# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-12

def too_much_screen_time(hours):
    total = 0

    for i, day in enumerate(hours):
        if day >= 10:
            return True

        if i < 5:
            if (hours[i] + hours[i+1] + hours[i+2]) / 3 >= 8:
                return True

        total += day    
    if total / 7 >= 6:
        return True

    return False
