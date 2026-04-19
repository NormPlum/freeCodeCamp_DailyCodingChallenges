# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-18

def find_sum(arr, target):
    subset = []
    last = []

    i = 0
    while i < len(arr):
        subset.append(arr[i])
        total = sum(subset)

        if total == target:
            return subset
        elif total < target:
            last.append(i)
            i += 1
        else:
            subset.pop()
            i += 1

        while i == len(arr):
            subset.pop()
            i = last[-1] + 1
            last.pop()
            if not last:
                break

    return "Sum not found"
