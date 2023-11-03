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

## Modifiying Values in a Dictionary
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

## A Dictionary of Similar Objects

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