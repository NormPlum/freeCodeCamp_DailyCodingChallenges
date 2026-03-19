# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-18

def sock_pairs(pairs, cycles):
    rules = {
        2: -1,
        3: +1,
        5: -1,
        10: +2,
    }
    socks = pairs * 2

    for cycle in range(1, cycles+1):
        for rule in rules:
            if cycle % rule == 0:
                socks += rules[rule]

    return int(socks / 2)
