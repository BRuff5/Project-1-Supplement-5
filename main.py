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
    
    if number % 2 != 0:  
        number *= 2
        print(f"Number is odd, multiplying by 2: {number}")
        
    """If the number is odd, multiply it by 2.
    Args:
        user_input: Recieves user_input
    Result:
        If user input is odd the it will be multiplyed by 2
    """
    
    if number % 3 == 0: 
        number //= 3
        print(f"Number is divisible by 3, dividing by 3: {number}")
        
    """If the number is divisible 3 divide it by 3
    Args:
        user_input: Recieves user_input
    Result:
        If user input is divisible 3 then divide number by 3
    """
        
    if number % 4 == 0:  
        number *= 4
        print(f"Number is divisible by 4, multiplying by 4: {number}")
        
    """If the number is divisible 4 divide it by 4
    Args:
        user_input: Recieves user_input
    Result:
        If user input is divisible 4 then divide number by 4
    """
    
    if number > 4:
        raise ValueError("The resulting number is greater than 4.")
    
    """If number is greater than 4
    Args:
        user_input: Recieves user_input
    Returns:
        informs the number is greater than 4
    """
    
    return number