### Date Created: 11/13/23

## Write a program to calculate the factorial of given number

# Function to calculate the factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Test the function with a specific number
number = 5
result = factorial(number)

# Print the result
print(f"The factorial of {number} is: {result}")
