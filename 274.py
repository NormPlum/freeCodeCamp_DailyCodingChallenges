# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-11

def get_oldest(people):
    oldest = []
    age = 0

    for person in people:
        if int(person["age"]) > age:
            age = int(person["age"])
            oldest = [person["name"]]
        elif int(person["age"]) == age:
            oldest.append(person["name"])

    return oldest
