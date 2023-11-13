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

# 7-5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person
# is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are 
# over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# prompt user to input age
#age_prompt = "\nPlease enter your age:"
#age_prompt += "\n(Enter 'quit' when you are finished). "

#while True:
#    user_input = input(age_prompt)

#    if user_input.lower() == 'quit':
#        break

#   age = int(user_input)

#    if age < 3:
#        print("Your ticket is free.")
#    elif 3 <= age <= 12:
#        print("Your ticket is $10.")
#    else:
#        print("Your ticket is $15.")

# 7-6 Three Exits: Write different version of either Exercise 7-4 or 7-5 that do each of the following at least once:
    # - Use a conditional test in the while statement to stop the loop
    # - Use an active variable to control how long the loop runs
    # - Use a break statement to exit the loop when the user enters a 'quit' value


