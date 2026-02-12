# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-12

def largest_difference(skater1, skater2):
    diff = {}
    for i in range(len(skater1)):
        diff[abs(skater1[i] - skater2[i])] = i
    sorted_diff = dict(sorted(diff.items()))
    sorted_values = list(sorted_diff.values())
    return sorted_values[-1] + 1
