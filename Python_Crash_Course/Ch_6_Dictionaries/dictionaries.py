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


