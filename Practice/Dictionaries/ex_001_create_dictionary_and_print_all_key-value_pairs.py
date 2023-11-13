# Date Created: 11/13/23

# Create a dictionary representing a person with keys 'name', 'age', and 'city
# Print each key-value pair.

person = {
    "name": "jake",
    "age": 25,
    "city": "dallas",
    }

for key, value in person.items():
    # Check if the value is a string before applying title()
    if isinstance(value, str):
        # Print key and capitalized value if it's a string
        print(f"{key.title()}: {value.title()}")
    else:
        # Print key and value as is if it's not a string (e.g., for integers)
        print(f"{key.title()}: {value}")