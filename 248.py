# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-15

def sort_and_swap(arr):
    result = []
    arr.sort()

    for i, num in enumerate(arr):
        if i > 0 and i % 3 == 0:
            previous = result[i-1]
            result[i-1] = num
            result.append(previous)
        else:
            result.append(num)

    return result
