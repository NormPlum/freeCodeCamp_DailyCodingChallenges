# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-10

def array_diff(arr1, arr2):
    diff = []

    for item in arr1:
        if item not in arr2:
            diff.append(item)

    for item in arr2:
        if item not in arr1:
            diff.append(item)

    diff.sort()
    return diff
