## PRACTICE ##

# Create a text based game that has decision trees

# Welcome message
username = input("Welcome to the text-based game, 'Sandbox!'\n"
      "To start, please enter your first name: ")

print(f"Hi {username}, let's get started!\n\n")

# Set up 3 player classes
player_classes = [
    {
        "name": "Knight",
        "description": "Strong defender, balanced fighter with good health.",
        "HP": 400,
        "ATK": 250,
        "DEF": 350
    },
    {
        "name": "Rogue",
        "description": "Agile, high attacker with lower defense but moderate health.",
        "HP": 300,
        "ATK": 400,
        "DEF": 200
    },
    {
        "name": "Wizard",
        "description": "Powerful spellcaster, fragile, but deals massive damage with spells.",
        "HP": 250,
        "ATK": 450,
        "DEF": 300
    }
]

# Prompt user to choose a player class

print("Choose a player class:")
for player_class in player_classes:
    print(f"{player_class['name']}:")
    print(f"   Description: {player_class['description']}")
    print(f"   HP: {player_class['HP']}")
    print(f"   ATK: {player_class['ATK']}")
    print(f"   DEF: {player_class['DEF']}")
    print()