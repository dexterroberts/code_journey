## PRACTICE ##

# Create a text based game that has decision trees

# Welcome message
username = input("Welcome to the text-based game, 'Sandbox!'\n"
      "To start, please enter your first name: ")

print(f"Hi {username}, let's get started!"\n\n)

# Have user choose from 3 player classes
knight = {
    "description" = "Strong defender, balanced fighter with good health.",
    "hp": "400",
    "atk": "250",
    "def": "350", 
}

rogue = {
    "description" = "Agile, high attacker with lower defense but moderate health.",
    "hp": "400",
    "atk": "250",
    "def": "350",
}

wizard = {
    "description" = "Wizard: Powerful spellcaster, fragile, but deals massive damage with spells.",
    "hp": "400",
    "atk": "250",
    "def": "350",
}

player_classes = [knight, rogue, wizard]

print(player_classes)

