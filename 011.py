# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-21

def mile_pace(miles, duration):
    time = duration.split(":")
    total = (int(time[0]) * 60) + int(time[1])
    one_mile = int(total / miles)
    minutes = int(one_mile / 60)
    seconds = int(one_mile % 60)
    return str(minutes).rjust(2, "0") + ":" + str(seconds).rjust(2, "0")
