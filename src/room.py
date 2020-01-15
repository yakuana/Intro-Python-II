# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, room_name, desc, items):
        self.room_name = room_name
        self.desc = desc 
        self.items = items 
    def __str__(self):
        return f"{self.room_name}'s description: \n{self.desc}"
        