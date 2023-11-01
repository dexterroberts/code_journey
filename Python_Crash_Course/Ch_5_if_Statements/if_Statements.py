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
# Admission for anyone under age 4 is free.
age = 12
if age < 4:
    print("Your admission cost is $0.")
# Admission for anyone between the ages of 4 and 18 is $25
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

