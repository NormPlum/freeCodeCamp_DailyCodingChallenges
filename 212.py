# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-10

def insert_into_array(arr, value, index):
    new_arr = []

    i = 0
    while i < max(len(arr), 1):
        if i == index:
            new_arr.append(value)
        if i in range(len(arr)):
            new_arr.append(arr[i])
        i += 1

    return new_arr
