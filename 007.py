# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-17

def find_target(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return "Target not found"
