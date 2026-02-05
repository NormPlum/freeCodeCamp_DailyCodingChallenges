# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-05

def count_change(change):
    total = sum(change)
    dollars = int(total / 100)
    cents = total % 100
    return f"${dollars}.{cents:02d}"
