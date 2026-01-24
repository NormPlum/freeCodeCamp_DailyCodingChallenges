# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-29

def burn_candles(candles, leftovers_needed):
    burned = candles
    leftovers = candles
    while leftovers >= leftovers_needed:
        candles = int(leftovers / leftovers_needed)
        leftovers %= leftovers_needed
        burned += candles
        leftovers += candles
    return burned
