# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, room_name, desc, room_items, players=None):
        self.room_name = room_name
        self.desc = desc 
        self.room_items = room_items 
        self.players = players 
    def __str__(self):
        return f"{self.room_name}'s description: \n{self.desc}"
