# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-23

from datetime import datetime

def get_direction(time1, time2):
    time1 = datetime.strptime(time1, "%H:%M")
    time2 = datetime.strptime(time2, "%H:%M")

    diff_backwards = time1 - time2
    diff_forwards = time2 - time1

    if diff_backwards.seconds > diff_forwards.seconds:
        return "forward"
    elif diff_backwards.seconds < diff_forwards.seconds:
        return "backward"
    else:
        return "equal"
