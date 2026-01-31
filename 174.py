# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-31

def get_sign(date_str):
    zodiac_dates = {
        "03-21:04-19": "Aries",
        "04-20:05-20": "Taurus",
        "05-21:06-20": "Gemini",
        "06-21:07-22": "Cancer",
        "07-23:08-22": "Leo",
        "08-23:09-22": "Virgo",
        "09-23:10-22": "Libra",
        "10-23:11-21": "Scorpio",
        "11-22:12-21": "Sagittarius",
        "12-22:01-19": "Capricorn",
        "01-20:02-18": "Aquarius",
        "02-19:03-20": "Pisces",
    }

    _, month, day = date_str.split("-")

    for zodiac in zodiac_dates:
        dates = zodiac.split(":")
        month1, day1 = dates[0].split("-")
        month2, day2 = dates[1].split("-")

        if month == month1 and day >= day1:
            return zodiac_dates[zodiac]
        elif month == month2 and day <= day2:
            return zodiac_dates[zodiac]
