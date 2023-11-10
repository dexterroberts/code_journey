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
for index, player_class in enumerate(player_classes):
    print(f"{index + 1}: {player_class['name']}")

# Return player class
choice = int(input("Enter the number of your choice: ")) - 1

if 0 <= choice < len(player_classes):
    selected_class = player_classes[choice]
    print(f"You have chosen {selected_class['name']} class.")
else:
    print("Invalid choice. Please select a valid player class.")

# Start journey