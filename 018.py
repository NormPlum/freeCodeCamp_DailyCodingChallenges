# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-28

def get_laptop_cost(laptops, budget):
    # Remove duplicates.
    laptops = list(set(laptops))
    # Sort in descending order.
    laptops.sort(reverse = True)

    for i, price in enumerate(laptops):
        if i == 1 and price <= budget:
            return price
        elif i > 1 and price <= budget:
            return price

    return 0
