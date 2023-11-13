# Date Created: 11/13/23

# Create a dictionary representing a person with keys 'name', 'age', and 'city
# Print each key-value pair.

person = {
    "name": "jake",
    "age": 25,
    "city": "dallas",
    }

for key, value in person.items():
    print(f"{key.title()}: {value.title()}")