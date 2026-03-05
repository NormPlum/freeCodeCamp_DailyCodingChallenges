# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-12

def battle(our_team, opponent):
    wins = [0, 0]

    our_words = our_team.split()
    their_words = opponent.split()

    for i in range(len(our_words)):
        us = get_score(our_words[i])
        them = get_score(their_words[i])

        if us > them:
            wins[0] += 1
        elif us < them:
            wins[1] += 1

    if wins[0] > wins[1]:
        return "We win"
    elif wins[0] < wins[1]:
        return "We lose"
    else:
        return "Draw"


def get_score(word):
    total_score = 0

    for char in word:
        score = ord(char.lower()) - 96
        if char.isupper():
            score *= 2
        total_score += score

    return total_score
