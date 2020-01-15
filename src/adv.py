from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

print("-" * 30)
print("Welcome to the Adventure Game!")
print("-" * 30)

# Make a new player object that is currently in the 'outside' room.

player = Player("John", room['outside'].room_name, room['outside'].desc)
print(f"\n{player}")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

gameOver = False

while (not gameOver):
    user_input = input("\nWhere would you like to go? \n[n] North [e] East [s] South [w] West [q] Quit: ")

    if (user_input == "q"):
        print("Thanks for playing the Adventure Game!\n")
        break
    elif (user_input not in ['n', 'e', 's', 'w']):
        print("\nPlease enter a valid direction to travel.") 
        continue

    if (player.room_name == "Outside Cave Entrance"): 
        # outside 
       
        if (user_input != 'n'):
            # player can only go north when outside, so user must enter [n]
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        else:
            player.room_name = room['outside'].n_to.room_name
            player.desc = room['outside'].n_to.desc

    elif (player.room_name == "Foyer"):
        # foyer 

        if (user_input == 'w'):
            # player cannot travel west from the foyer 
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        elif (user_input == 's'):
            player.room_name = room['foyer'].s_to.room_name
            player.desc = room['foyer'].s_to.desc
        elif (user_input == 'n'):
            player.room_name = room['foyer'].n_to.room_name
            player.desc = room['foyer'].n_to.desc
        elif (user_input == 'e'):
            player.room_name = room['foyer'].e_to.room_name
            player.desc = room['foyer'].e_to.desc

    elif (player.room_name == "Grand Overlook"):
        # overlook 
        
        if (user_input != 's'):
            # player can only go south when at overlook, so user must enter [s]
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        else:
            player.room_name = room['overlook'].s_to.room_name
            player.desc = room['overlook'].s_to.desc

    elif (player.room_name == "Narrow Passage"):
        # narrow 

        if (user_input == 's' or user_input == 'e'):
            # player cannot travel south or east from the narrow passage  
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        elif (user_input == 'n'):
            player.room_name = room['narrow'].n_to.room_name
            player.desc = room['narrow'].n_to.desc
        elif (user_input == 'w'):
            player.room_name = room['narrow'].w_to.room_name
            player.desc = room['narrow'].w_to.desc

    elif (player.room_name == "Treasure Chamber"):
        # treasure 
        
        if (user_input != 's'):
            # player can only go south when at tresure, so user must enter [s]
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        else:
            player.room_name = room['treasure'].s_to.room_name
            player.desc = rroom['treasure'].s_to.desc

    print(f"\n{player}")
