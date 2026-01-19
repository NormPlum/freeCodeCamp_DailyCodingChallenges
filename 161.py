# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-18

def gets_free_shipping(cart, minimum):
    prices = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95,
    }

    total = 0
    for item in cart:
        total += prices[item]
    
    return total >= minimum
