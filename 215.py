# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-13

from datetime import datetime, timedelta
import math

def calculate_parking_fee(park_time, pickup_time):
    park = datetime.strptime(park_time, "%H:%M")
    pickup = datetime.strptime(pickup_time, "%H:%M")

    diff = pickup - park
    hours = math.ceil(diff.seconds / 60 / 60)
    overnight = abs(diff.days)

    fee = max((hours * 3) + (overnight * 10), 5)
    return "$" + str(fee)
