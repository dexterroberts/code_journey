#### Date Created: 11/1/23 ###
#### Chapter 5: if Statements ###

### if Statements

## Simple if Statements: The simplest kind of if statement has one test and one action:

# if conditional_test:
    # do something

# EXAMPLE 1 #
#age = 19
#if age >= 18:
#    print("You are old enough to vote!")
#    print("Have you registered to vote yet?")

## if-else Statements

# EXAMPLE 2 #
#age = 17
#if age >= 18:
#    print("You are old enough to vote!")
#else:
#    print("Sorry, you are too young to vote.\nPlease register to vote as soon as you turn 18!")

# if-elife-else Chain

# EXAMPLE 3 #
# Admission for anyone under age 4 is free.
#age = 12
#if age < 4:
#    print("Your admission cost is $0.")
# Admission for anyone between the ages of 4 and 18 is $25
#elif age < 18:
#    print("Your admission cost is $25.")
# Admission for anyone age 18 or older is $40
#else:
#    print("Your admission cost is $40.")

# EXAMPLE 3a #
#age = 12

#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#else:
#    price = 40

#print(f"Your admission cost is ${price}.")


## Testing Multiple Conditions

#requested_toppings = ["mushrooms", "extra cheese"]

#if "mushrooms" in requested_toppings:
#    print("Adding mushrooms.")
#if "pepperoni" in requested_toppings:
#    print("Adding pepperoni.")
#if "extra cheese" in requested_toppings:
#    print("Adding extra cheese")

#print("Finished making your pizza!")

## TRY IT YOURSELF ##
# 5-3 Alien Color #1

#alien_color = "green"
#if alien_color == "green":
#    print("You just earned 5 points!")

#alien_color = "blue"                    # make the if statement not pass the test
#if alien_color = "green":
#    print("You just earned 5 points!")

# 5-4 Alien Colors #2
#alien_color = "green"
#if alien_color == "green":
#    print("You just earned 5 points!")
#else:
#    print("You just earned 10 points!")

# 5-5 Alien Colors #3
#print("Green Alien")
#alien_color_1 = "green"

#if alien_color_1 == "green":
#    print("You just earned 5 points.")
#elif alien_color_1 == "blue":
#    print("You just earned 10 points.")
#elif alient_color_1 == "red":
#    print("You just earned 15 points.\n")

#print("Blue Alien")
#alien_color_2 = "blue"

#if alien_color_2 == "green":
#    print("You just earned 5 points.")
#elif alien_color_2 == "blue":
#    print("You just earned 10 points.")
#elif alient_color_2 == "red":
#    print("You just earned 15 points.\n")

#print("Red Alien")
#alien_color_3 = "red"

#if alien_color_3 == "green":
#    print("You just earned 5 points.")
#elif alien_color_3 == "blue":
#    print("You just earned 10 points.")
#elif alien_color_3 == "red":
#    print("You just earned 15 points.\n")

# 5-6 Stages of Life
#age = 21

#if age < 2:
#    print("You're a baby!")
#elif age >= 2 and age < 4:
#    print("You're a toddler!")
#elif age >= 4 and age < 13:
#    print("You're a kid!")
#elif age >= 13 and age < 20:
#    print("You're a teenager!")
#elif age >= 20 and age < 65:
#    print("You're an adult!")
#else:
#    print("You're an elder!")

# 5-7 Favorite Fruit

#favorite_fruits = ["watermelon", "strawberry", "peach", "apple"]

#if "watermelon" in favorite_fruits:
#    print(f"You really like {favorite_fruits[0]}!")
#else:
#    print("Looks like you don't have any watermelons!")

## Using if Statements with Lists

## Checking for Special Items

#requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

#for requested_topping in requested_toppings:
#    print(f"Adding {requested_topping}.")

#print("\nFinished making your pizza!")
#for requested_topping in requested_toppings:
#    if requested_topping == "green peppers":
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {requested_topping}.")

#print("\nFinished making your pizza!")

## Checking That a List Is Not Empty
