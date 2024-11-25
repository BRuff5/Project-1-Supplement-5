import random
import math

def square_root(num):
    if num < 0:
        raise ValueError("INVALID NUMBER: Cannot calculate the square root of a negative number.")
    return math.sqrt(num)

    """Return the square root of a number or raise an exception if negative
    Args:
        num: The argument passed to the function, which must be a float or an integer. It represents the number for which the square root is to be calculated.
    Returns:
        A float value, which is the square root of num.
    Raises:
        ValueError is explicitly raised if num is negative to indicate invalid input.
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

def divisible_numbers(n):
    if n == 0:
        raise ValueError("Cannot divide by zero.")
    return [i for i in range(1, 11) if i % n == 0]

"""Return a list of integers between 1 and 10 that are divisible by n.
Args:
    List: Integers between 1 and 10 that are divisible by n
Returns:
    Gives results divisible by n and informs if cannot divide by 0
"""

def main():
    user_input = input("Enter a number to find its square root: ")
    
    """User_input
    Args:
        Input: user_input
    Returns:
        Ask user what number they want to square root
    """
    
    try:
        num = float(user_input)
        root = square_root(num)
        print(f"The square root of {num} is {root}")
    except ValueError as e:
        print(e)
        
    """
    Calculate the square root of a given number.
    Args:
        user_input (str): The input value provided by the user, which is expected to be a number.
    Returns:
        float: The square root of the input number if valid.
        str: An error message if the input is not valid.
    Raises:
        ValueError: If the input cannot be converted to a float.
    """

    try:
        result = process_random_integer()
        print(f"The final result after processing is: {result}")
    except ValueError as e:
        print(e)
        
    """
    Generate and process a random integer within a given range.
    Args:
        min_value (int): The minimum value of the random integer (inclusive). Default is 0.
        max_value (int): The maximum value of the random integer (inclusive). Default is 100.
    Returns:
        int: The processed result after performing operations on the random integer.
    Raises:
        ValueError: If the range defined by min_value and max_value is invalid.
    """