# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-03

def get_browser_history(commands):
    history = []
    index = 0

    for command in commands:
        if command == "Back":
            if index > 0:
                index -= 1
        elif command == "Forward":
            if index < len(history)-1:
                index += 1
        else:
            history = history[:index+1]
            history.append(command)
            index = len(history)-1

    return [history, index]
