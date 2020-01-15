# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room 

class Player(Room):
    def __init__(self, name, room_name, desc, items):
        super().__init__(room_name, desc, items)
        self.name = name
    def __str__(self):
        return f"{self.name} is located {self.room_name} \nRoom description: \n{self.desc}"