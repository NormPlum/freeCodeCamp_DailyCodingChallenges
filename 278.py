# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-15

def format_coffee_order(order):
    prices = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    items = []
    total = 0

    for item in prices:
        if item in order:
            items.append(item)
            total += prices[item]

    items_string = " + ".join(items)
    return f"{items_string}: ${total:.2f}"
