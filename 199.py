# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-25

def find_differences(arr):
    result = []
    for i in range(0, len(arr)-1):
        result.append(arr[i+1] - arr[i])
    result.append(0)
    return result
