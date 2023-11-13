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

# Take user input for the number
user_input = input("Enter a number to find its factorial: ")

# Convert the user input to an integer
number = int(user_input)

# Calculate the factorial
result = factorial(number)

# Print the result
print(f"The factorial of {number} is: {result}")
