# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-24

def battle(my_army, opposing_army):
    if len(my_army) < len(opposing_army):
        return "We retreated"
    elif len(my_army) > len(opposing_army):
        return "Opponent retreated"
    
    my_wins = 0
    for i in range(len(my_army)):
        my_value = get_value(my_army[i])
        opposing_value = get_value(opposing_army[i])
        if my_value > opposing_value:
            my_wins += 1
        elif my_value < opposing_value:
            my_wins -= 1
    
    if my_wins > 0:
        return "We won"
    elif my_wins < 0:
        return "We lost"
    else:
        return "It was a tie"


def get_value(char):
    if char.isalpha():
        unicode = ord(char)
        if char.isupper():
            return unicode - 38
        else:
            return unicode - 96
    elif char.isdigit():
        return int(char)
    else:
        return 0
