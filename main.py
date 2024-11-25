import random
import math

def square_root(num):
    if num < 0:
        raise ValueError("INVALID NUMBER: Cannot calculate the square root of a negative number.")
    return math.sqrt(num)

    """Return the square root of a number or raise an exception if negative
    Args:
        Returns number
    Return:
        Squeres a number and if number is negative invalid response message appears
    """
    
def process_random_integer():
    number = random.randint(1, 100)
    print(f"Random number generated: {number}")
    
    """Pick a random integer between 1 and 100
    Args:
        Pulls imported random number
    Result:
        Displays random number that was generated
    """