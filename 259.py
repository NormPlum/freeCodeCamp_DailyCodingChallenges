# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-26

def explode_fizzbuzz(target_z_count):
    string = "fizzbuzz"
    step = 1

    while True:
        new_string = ""
        for i, char in enumerate(string):
            pos = i + 1
            if pos % 3 == 0 and pos % 5 == 0:
                new_string += "fizzbuzz"
            elif pos % 3 == 0:
                new_string += "fizz"
            elif pos % 5 == 0:
                new_string += "buzz"
            else:
                new_string += char

        if new_string.count("z") < target_z_count:
            string = new_string
            step += 1
        else:
            return step
