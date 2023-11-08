## PRACTICE ##

# create a dictionary

user = {
    "first_name": "jack",
    "last_name": "robinson",
    "username": "jrob",
    "hobbies": ["baseball", "hiking", "gym"]
    }

user_1 = {
    "first name": "sara",
    "last_name": "taylor",
    "username": "saratay",
    "hobbies": ["photography", "baking", "hiking"]
    }

users = [user, user_1]

unique_hobbies = set()

for user_data in users:
    unique_hobbies.update(user_data["hobbies"])

unique_hobbies_list = list(unique_hobbies)

formatted_hobbies = ", ".join(unique_hobbies_list)

print(f"Unique Hobbies: {formatted_hobbies.title()}")