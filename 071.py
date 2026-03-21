# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-20

def calculate_tips(meal_price, custom_tip):
    result = []
    price = float(meal_price[1:])
    tips = [0.15, 0.2]
    tips.append(int(custom_tip[:-1]) / 100)

    for tip in tips:
        amount = price * tip
        result.append(f"${amount:.2f}")

    return result
