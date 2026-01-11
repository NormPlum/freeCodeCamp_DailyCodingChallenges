# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-12

def is_valid_number(n, base):
    # The highest base with only numbers.
    BASE_LIMIT = 10
    # The unicode value for the uppercase letter 'A'.
    UNICODE_A = 65

    base_digits = []

    # Populate the list of base digits.
    numbers = min(base, BASE_LIMIT)
    for i in range(numbers):
        base_digits.append(str(i))

    if base > BASE_LIMIT:
        letters = base - BASE_LIMIT
        for j in range(UNICODE_A, letters + UNICODE_A):
            base_digits.append(chr(j))
    
    # Check each character in the number.
    for char in n:
        if char.upper() not in base_digits:
            return False
    
    return True
