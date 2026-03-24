# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-24

def passing_count(scores, passing_score):
    count = 0
    for score in scores:
        if score >= passing_score:
            count += 1
    return count
