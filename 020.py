# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-30

def find_duplicates(arr):
    duplicates = []

    while len(arr) > 0:
        num = arr.pop()
        if num in arr:
            duplicates.append(num)

    duplicates = list(set(duplicates))
    duplicates.sort()
    return duplicates
