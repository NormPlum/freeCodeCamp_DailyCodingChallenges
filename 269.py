# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-06

def get_allergen_friendly_meals(meals, allergens):
    safe = []

    for meal in meals:
        food = meal[0]
        food_allergens = meal[1]

        ok = True
        for allergen in allergens:
            if allergen in food_allergens:
                ok = False
        if ok:
            safe.append(food)

    return safe
