### Date Created: 11/5/23
### Chapter 7: User Input and while Loops

## Introducing while Loops
#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1

# Letting the User Choose When to Quit
#prompt = "\nTell me something, and I will repeat it back to you."
#prompt += "\nEnter 'quit to end the program.' "

#message = ""
#while message != 'quit':
#    message = input(prompt)

#if message == 'quit':
#    print("\nThanks for playing!")

# Using break to Exit a Loop
#prompt = "\nPlease enter the name of a city you have visited: "
#prompt += "\n(Enter 'quit' when you are finished). "

#while True:
#    city = input(prompt)

#    if city == "quit":
#        break
#    else: print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop

# print odd numbers that are less than 10
#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue

#    print(current_number)

# TRY IT YOURSELF #
# 7-4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
# enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

# prompt user for input
#toppings = "\nPlease enter the topping you wish to add to your pizza: "
#toppings += "\n(Enter 'quit' when you are finished). "

#while True:
#    pizza_toppings = input(toppings)

#    if pizza_toppings == "quit":
#        break
#    else:
#        print(f"I will add {pizza_toppings} to your pizza!")

#print("\nThanks! Your pizza will be out shortly!")


