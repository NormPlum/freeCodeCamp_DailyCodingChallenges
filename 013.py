# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-23

def is_unnatural_prime(n):
    n = abs(n)
    if n < 2:
        return False
    else:
        return is_prime(n)


# Copied from https://www.w3schools.com/java/java_howto_check_prime_num.asp
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
