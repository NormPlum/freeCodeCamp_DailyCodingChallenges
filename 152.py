# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-01-09

def is_circular_prime(n):
    numbers = list(str(n))

    for i in range(len(numbers)):
        # Rotate digits.
        first = numbers.pop(0)
        numbers.append(first)

        # Get integer number.
        string = ""
        for j in numbers:
            string += j
        number = int(string)

        # Check if prime.
        if not is_prime(number):
            return False
    
    return True


# Copied from https://www.w3schools.com/java/java_howto_check_prime_num.asp
def is_prime(n):
    i = 2
  
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
      
    return True
