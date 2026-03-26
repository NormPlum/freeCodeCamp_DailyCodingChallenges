# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-26

def get_movie_night_cost(day, showtime, number_of_tickets):
    prices = {
        "Monday": 10,
        "Tuesday": 5,
        "Wednesday": 10,
        "Thursday": 10,
        "Friday": 12,
        "Saturday": 12,
        "Sunday": 12,
    }

    cost = prices[day] * number_of_tickets

    if day != "Tuesday":
        colon = showtime.find(":")
        if showtime[-2:] == "am" or int(showtime[:colon]) < 5:
            cost -= 2 * number_of_tickets

    return f"${cost}.00"
