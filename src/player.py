# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room 

class Player():
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items 

    def __str__(self):
        return f"{self.name}'s location is {self.current_room}."

    def print_items(self): 
        if (self.items != []):
            print(f"\n{self.name} has the following items:")
            for item in self.items: 
                print(item)
        else: 
            print("You do not have any items currently.") 
            
    def add_item(self, item): 
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
