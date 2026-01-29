# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-28

def flatten(arr):
    return flatten_recursive(arr, [])

def flatten_recursive(arr, flat):
    for item in arr:
        if type(item) is list:
            flat = flatten_recursive(item, flat)
        else:
            flat.append(item)
    return flat
