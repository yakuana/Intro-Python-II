from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons", 
        [
            Item("backpack", "Something to hold your treasure"), 
            Item("shades", "Protect your eyes from harmful rays")
        ]),

    'foyer':    Room(
        "Foyer", 
        """Dim light filters in from the south. Dusty passages run north and east.""", 
        [
            Item("match", "Just one. Don't lose it."), 
            Item("book", "Something to read or not to read."), 
            Item("knife", "It's sharp. It's pointy. Be careful.")
        ]),

    'overlook': Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", 
        [
            Item("rope", "Looks like the mice beat you to this one. Looks more like a thread than a rope."), 
            Item("mirror", "You look great!")
        ]),

    'narrow':   Room(
        "Narrow Passage", 
        """The narrow passage bends here from west to north. The smell of gold permeates the air.""", 
        [
            Item("bottle", "There seems to be a mystery liquid at the bottom. It's blue... or purple, maybe red? Definitely orange!"), 
            Item("lighter", "*flick* *flick* That's hot!")
        ]),

    'treasure': Room(
        "Treasure Chamber", 
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", 
        [
            Item("note", "The Earth is flat I tell ya! In 1684 I asked the moon and the moon said the dandiest of things. For starters, the Earth is indeed FLAT and spheres are alien propaganda for their inevitable regime. Don't believe me? Keep reading...")
        ]),
}

# Item arrays initial content 

""" outside 
[
    Item("backpack", "Something to hold your treasure"), 
    Item("shades", "protect your eyes from harmful rays")
]

foyer 
[
    Item("match", "Just one. Don't lose it."), 
    Item("book", "Something to read or not to read."), 
    Item("knife", "It's sharp. It's pointy. Be careful.")
]

overlook 
[
    Item("rope", "Looks like the mice beat you to this one. Looks more like a thread than a rope."), 
    Item("mirror", "You look great!")
]

narrow 
[
    Item("bottle", "There seems to be a mystery liquid at the bottom. It's blue... or purple, maybe red? Definitely orange!"), 
    Item("lighter", "*flick* *flick* That's hot!")
]

treasure 
[
    Item("note", "The Earth is flat I tell ya! In 1684 I asked the moon and the moon said the dandiest of things. For starters, the Earth is indeed FLAT and spheres are alien propaganda for their inevitable regime. Don't believe me? Keep reading...")
] """


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

player = Player("John", room['outside'].room_name)

print(f"\n{player}")
player.print_items()
print(f"\n{room['outside']}")


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

while (True):

    # user direction input 
    user_dir = input("\nWhere would you like to go? \n[n] North [e] East [s] South [w] West [q] Quit: ")

    if (user_dir == "q"):
        print("Thanks for playing the Adventure Game!\n")
        break
    elif (user_dir not in ['n', 'e', 's', 'w']):
        print("\nPlease enter a valid direction to travel.") 
        continue

    if (player.current_room == "Outside Cave Entrance"): 
       
        if (user_dir != 'n'):
            # player can only go north when outside, so user must enter [n]
            print(f"\nLooks like you cannot travel [{user_dir}]. Try a different direction.")
            continue 
        else:
            player.current_room = room['outside'].n_to.room_name
            
    elif (player.current_room == "Foyer"):

        if (user_dir == 'w'):
            # player cannot travel west from the foyer 
            print(f"\nLooks like you cannot travel [{user_dir}]. Try a different direction.")
            continue 
        elif (user_dir == 's'):
            player.current_room = room['foyer'].s_to.room_name 
        elif (user_dir == 'n'):
            player.current_room = room['foyer'].n_to.room_name
        elif (user_dir == 'e'):
            player.current_room = room['foyer'].e_to.room_name

    elif (player.current_room == "Grand Overlook"):
        
        if (user_dir != 's'):
            # player can only go south when at overlook, so user must enter [s]
            print(f"\nLooks like you cannot travel [{user_dir}]. Try a different direction.")
            continue 
        else:
            player.current_room = room['overlook'].s_to.room_name

    elif (player.current_room == "Narrow Passage"):

        if (user_dir == 's' or user_dir == 'e'):
            # player cannot travel south or east from the narrow passage  
            print(f"\nLooks like you cannot travel [{user_dir}]. Try a different direction.")
            continue 
        elif (user_dir == 'n'):
            player.current_room = room['narrow'].n_to.room_name
        elif (user_dir == 'w'):
            player.current_room = room['narrow'].w_to.room_name

    elif (player.current_room == "Treasure Chamber"):

        if (user_dir != 's'):
            # player can only go south when at tresure, so user must enter [s]
            print(f"\nLooks like you cannot travel [{user_dir}]. Try a different direction.")
            continue 
        else:
            player.current_room = room['treasure'].s_to.room_name
        
    print(f"\n{player}")

    '''
        Matches the player's room to a room in the room object using keys. 
        Gives the player an opportunity to acquire an item from that room. 
        Informs the player of the items they now have. 
    '''
    for key in room: 
        if key in player.current_room.lower():
            print(f"\n{player.current_room} has the following items:")

            # prints the items in the room 
            for item in room[key].room_items: 
                print(item)
            
            # user items acquiration 
            user_item = input("\nWould you like to take an item from this room? \nIf yes, type [get] followed by the name of the item. \nIf you would like to leave an item, type [drop] followed by the item name. \nIf neither, type [no].\n")

            if ("no" not in user_item): 
                
                # will determine whether the user successfully added or removed an item 
                successful = False

                # make items list 
                user_item = user_item.split()

                for item in room[key].room_items: 
                    if (user_item[0] == "get" and user_item[1] == item.item_name): 
                        player.add_item(item)
                        room[key].remove_item(item)
                        item.on_take()
                        successful = True 
                    elif (user_item[0] == "drop"): 
                        for obj in player.items: 
                            if (obj.item_name == user_item[1]):
                                player.remove_item(obj)
                                room[key].add_item(obj)
                                obj.on_drop()
                                successful = True 
            
                if (not successful):
                    print("I'm sorry, an error has occured. You have lost your opportunity to steal and must move on.")
                
                # inventory check option
                inventory = input("\nWould you like to view your inventory? \nIf yes, type [i]. \nIf no, type [no].\n")

                if (inventory == "i"):
                    player.print_items()

            # prints player's current room description 
            print(f"\n{room[key]}")
