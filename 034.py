# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-13

def find_missing_numbers(arr):
    missing = []

    arr = list(set(arr))
    arr.sort()

    for i in range(1, arr[-1]):
        if i not in arr:
            missing.append(i)

    return missing
