# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-22

def count_medals(winners):
    medals = {}

    for event in winners:
        for i, country in enumerate(event):
            if country not in medals:
                medals[country] = [0, 0, 0, 0]
            medals[country][i] += 1
            medals[country][3] += 1

    medals = dict(sorted(medals.items(), key=lambda c: (-c[1][0], c[0])))

    csv = "Country,Gold,Silver,Bronze,Total"
    for country in medals:
        csv += "\n" + country
        for count in medals[country]:
            csv += "," + str(count)

    return csv
