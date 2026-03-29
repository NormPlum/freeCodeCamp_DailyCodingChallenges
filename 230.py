# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-28

def pascal_row(n):
    triangle = []

    for num in range(1, n+1):
        if num == 1:
            triangle.append([1])
        elif num == 2:
            triangle.append([1, 1])
        else:
            row = [1]
            for i in range(1, len(triangle[num-2])):
                row.append(triangle[num-2][i-1] + triangle[num-2][i])
            row.append(1)
            triangle.append(row)

    return triangle[n-1]
