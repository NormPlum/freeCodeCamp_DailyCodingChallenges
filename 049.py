# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-28

def get_headings(csv):
    headings = csv.split(",")
    return [heading.strip() for heading in headings]
