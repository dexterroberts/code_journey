### Date Created: 11/01/23
### Chapter 6: Dictionaries

## A Simple Dictionary ## 

#alien_0 = {"color": "green", "points": 5}

#print(alien_0["color"])
#print(alien_0["points"])

## Working with Dictionaries ##

#alien_0 = {"color": "green", "points": 5}

#new_points = alien_0["points"]
#print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs #
#alien_0 = {"color": "green", "points": 5}
#print(alien_0)

#alien_0["x_position"] = 0
#alien_0["y_position"] = 25
#print(alien_0)

## Starting with an Empty Dictionary ##

#alien_0 = {}

#alien_0["color"] = "green"
#alien_0["points"] = 5

#print(alien_0)

## Modifiying Values in a Dictionary ##

#alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
#print(f"Original position: {alien_0["x_position"]}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
#if alien_0["speed"] == "slow":
#    x_increment = 1
#elif alien_0["speed"] == "medium":
#    x_increment = 2
#else:
    # This must be a fast alien.
#    x_increment = 3

# The new position is the old position plus the increment.
#alien_0["x_position"] = alien_0["x_position"] + x_increment

#print(f"New position: {alien_0["x_position"]}")


## Removing Key-Value Pairs
#alien_0 = {"color": "green", "points": 5}
#print(alien_0)

#del alien_0["points"]
#print(alien_0)

## A Dictionary of Similar Objects ##

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#print(favorite_languages)

#language = favorite_languages["sarah"].title()
#print(f"Sarah's favorite language is {language}.")

## Using get() to Access Values
#alien_0 = {"color": "green", "speed": "medium:"}
#print(alien_0["points"])  # KeyError: "points" - points was not assigned and you get this error

#point_value = alien_0.get("points", "No point value assigned.")
#print(point_value)

## TRY IT YOURSELF ##
# 6-1 Person

#person = {"first_name": "jake", "last_name": "winters", "age": 27, "city": "jacksonville"}
#print(f"First Name: {person['first_name'].title()}")
#print(f"Last Name: {person['last_name'].title()}")
#print(f"Age: {person["age"]}")
#print(f"City: {person["city"].title()}")

# 6-2 Favorite Numbers
#favorite_number = {"jenny": 6, "sarah": 9, "max": 3, "rex": 7, "dave": 5}

#print(favorite_number["dave"])
#print(favorite_number["jenny"])
#print(favorite_number["max"])
#print(favorite_number["rex"])
#print(favorite_number["sarah"])

# 6-3 Glossary
#python_definitions = {
#    "variable": "a container of which a value is assigned.", 
#    "for_loop": "iterates over a sequence and executes a block of code for each element in the sequence.",
#    "list": "an ordered collection of items, allowing duplicates and mutable.",
#    "dictionary": "a collection of key-value pairs, allowing fast access to values using unique keys.",
#    "pop": "a method used to remove and return an element from a list or dictionary by its index or key."
#    }

#print(f"Variable: {python_definitions["variable"]}")
#print(f"for Loop: {python_definitions["for_loop"]}")
#print(f"List: {python_definitions["list"]}")
#print(f"Dictionary: {python_definitions["dictionary"]}")
#print(f"Pop: {python_definitions["pop"]}")

## Looping Through a Dictionary ##

#user_0 = {
#    "user_name": "efermi",
#    "first": "enrico",
#    "last": "fermi",
#}

#for key, value in user_0.items():
#    print(f"\nKey: {key}")
#    print(f"Value: {value}")

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}.")

# !! REMEMBER: As it worked through each pair the KEY is assigned to the VARIABLE 'name' (cont'd)
# and the VALUE is assigned to the VARIABLE 'language'

## Looping Through All the Keys in a Dictionary ##

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#for name in favorite_languages.keys():
#    print( name.title())

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#friends = ["phil", "sarah"]
#for name in favorite_languages.keys():
#    print(f"Hi {name.title()}.")

#    if name in friends:
#        language = favorite_languages[name].title()
#        print(f"\t{name.title()}, I see you love {language}!")

#if "erin" not in favorite_languages.keys():
#    print("Erin, please take our poll!")

## Looping Through a Dictionary's Keys in a Particular Order ##

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking the poll.")


## Looping Through All Values in a Dictionary ##

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

# using set() to identify unique items in the collection and builds a set from those items

#favorite_languages = {
#    "jen": "python", 
#    "sarah": "c", 
#    "edward": "rust", 
#    "phil": "python"
#    }

#print("The following languages have been mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())

## TRY IT YOURSELF ##

# 6-4 Glossary 2
#python_definitions = {
#    "variable": "a container of which a value is assigned.", 
#    "for_loop": "iterates over a sequence and executes a block of code for each element in the sequence.",
#   "list": "an ordered collection of items, allowing duplicates and mutable.",
#    "dictionary": "a collection of key-value pairs, allowing fast access to values using unique keys.",
#    "pop": "a method used to remove and return an element from a list or dictionary by its index or key."
#    }

#for term, definition in python_definitions.items():
#    print(f"{term}: {definition.title()}")

#python_definitions["tuple"] = "an ordered and immutable collection of items."
#print(python_definitions)

## NESTING ##

# A List of Dictionaries #

#alien_0 = {"color": "green", "points": 5}
#alien_1 = {"color": "yellow", "points": 10}
#alien_2 = {"color": "red", "points": 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

# Make an empty list for storing aliens
#aliens = []

# Make 30 green aliens
#for alien_number in range(30):
#    new_alien = {"color": "green", "points": 5, "speed": "slow"}
#    aliens.append(new_alien)

# Show the first 5 aliens
#for alien in aliens[:5]:
#    print(alien)
#print("...")

# Show how many aliens have been created
#print(f"Total number of aliens: {len(aliens)}")

# Change the first 3 aliens to yellow, medium-speed aliens worth 10 pts ea. 
# Make an empty list for storing aliens
#aliens = []

# Make 30 green aliens
#for alien_number in range(30):
#    new_alien = {"color": "green", "points": 5, "speed": "slow"}
#    aliens.append(new_alien)

#for alien in aliens[:3]:
#    if alien["color"] == "green":
#        alien["color"] = "yellow"
#        alien["speed"] = "medium"
#        alien["points"] = 10

# Show the first 5 aliens
#for alien in aliens[:5]:
#    print(alien)
#print("...")

# A List in a Dictionary

# Ordering pizza example
# Store information abouta pizza being ordered
#pizza = {
#    "crust": "thick",
#    "toppings": ["mushrooms", "extra cheese"],
#    }

# Summarize the order
#print(f"You ordered a {pizza["crust"]}-crust pizza "
#      "with the following toppings:")

#for topping in pizza["toppings"]:
#    print(f"\t{topping}")

# Favorite languages example

#favorite_languages = {
#    "jen": ["python", "rust"],
#    "sarah": ["c"],
#    "edward": ["rust", "go"],
#    "phil": ["python", "haskell"], 
#    }

#for name, languages in favorite_languages.items():
#    print(f"\n{name.title()}'s favorite languages are:")
#    for language in languages:
#        print(f"\t{language.title()}")

# PERSONAL SANDBOX EXAMPLE

# list employees and employee emails
employee_list = {
    "joey": ["joey@company.com", "joey@personal.com"],
    "sam": ["sam@company.com", "sam@personal.com"],
    "lisa": ["lisa@company.com", "lisa@personal.com"],
    "pam": ["pam@company.com", "pam@personal.com"],
    }

for employee, emails in employee_list.items():
    print(f"\n{employee.title()} emails are:")
    for email in emails:
        print(f"\t{email}")
