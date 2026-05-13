# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-13

def find_offender(arr):
    for i in range(len(arr)):
        arr2 = arr.copy()
        arr2.pop(i)
        arr3 = arr2.copy()
        arr3.sort()
        if arr2 == arr3:
            return i
