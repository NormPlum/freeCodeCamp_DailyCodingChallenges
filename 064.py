# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-13

def to_12(time):
    hour = time[:2]
    minute = time[2:]
    
    if int(hour) <= 12:
        if hour == "00":
            hour = "12"
        return str(int(hour)) + ":" + minute + " AM"
    else:
        return str(int(hour) - 12) + ":" + minute + " PM"
