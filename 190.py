# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-16

def get_semifinal_matchups(teams):
    totals = {}
    for team in teams:
        team_details = team.split(": ")
        scores = team_details[1].split("-")
        totals[int(scores[0]) * 3 + int(scores[1]) * 2 + int(scores[2]) * 1] = team_details[0]
    sorted_totals = dict(sorted(totals.items(), reverse=True))
    countries = list(sorted_totals.values())
    return "The semi-final games will be " + countries[0] + " vs " + countries[3] + " and " + countries[1] + " vs " + countries[2] + "."
