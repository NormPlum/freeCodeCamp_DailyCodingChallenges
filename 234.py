# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-01

def fix_prank_number(arr):
    diff = {}
    for i in range(1, len(arr)):
        diff[i] = arr[i] - arr[i-1]

    # Get most frequent number.
    diff_values = list(diff.values())
    pattern = max(set(diff_values), key=diff_values.count)

    # Get incorrect index.
    for i in diff:
        if diff[i] != pattern:
            if i+1 not in diff or diff[i+1] != pattern:
                incorrect = i
            else:
                incorrect = i-1
            break

    if incorrect != 0:
        arr[incorrect] = arr[incorrect-1] + pattern
    else:
        arr[incorrect] = arr[incorrect+1] - pattern

    return arr
