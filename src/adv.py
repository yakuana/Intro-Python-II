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

# Make a new player object that is currently in the 'outside' room.

player = Player("John", room['outside'].room_name, room['outside'].desc)
print(f"{player}")

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

    # switch(player1.room.room_name) {
    #     case "Outside Cave Entrance": 
    #         user_input = input("Where would you like to go? \n[n] North [e] East [s] South [w] West") 
    #         while (user_input != 'n'):
    #             print(f"Looks like you cannot go [{user_input}]. Pick a different direction to travel.")
    #             user_input = input("Where would you like to go? \n[n] North [e] East [s] South [w] West") 
    #         player1.room = room['outside'].n_to
    #         gameOver = True
    #         break 
    # }

    # if (user_input == 'n'):
    #     else if (user_input == 'e'):
    #     else if (user_input == 's'):
    #     else if (user_input == 'w'):

    if (user_input == "q"):
        print("Thanks for playing the Adventure Game!\n")
        break
    elif (user_input not in ['n', 'e', 's', 'w']):
        print("\nPlease enter a valid direction to travel.") 
        continue

    if (player.room_name == "Outside Cave Entrance"): 
        # you can only go north when outside, so user must enter [n]

        if (user_input != 'n'):
            print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
            continue 
        else:
            player.room_name = room['outside'].n_to.room_name
            player.desc = room['outside'].n_to.room_name

    # elif (player.room_name == "Foyer"):

    #     if (user_input == 'w'):
    #         print(f"\nLooks like you cannot travel [{user_input}]. Try a different direction.")
    #         continue 
    #     elif (user_input == 's'):
    #         player.room = room['foyer'].s_to
            
    #     else if (user_input == 'n'):
    #         player.room = room['foyer'].n_to 
           
    #     else if (user_input == 'e'):
    #         player.room = room['foyer'].e_to 
           

    # else if (player.room == "Grand Overlook"):
    # else if (player.room == "Narrow Passage"):
    # else if (player.room == "Treasure Chamber"):

    print(f"{player}")
