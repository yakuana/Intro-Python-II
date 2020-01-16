from room import Room 

class Item(): 
    def __init__(self, item_name, item_desc):
        self.item_name = item_name 
        self.item_desc = item_desc
    def __str__(self):
        return f"~ {self.item_name}: {self.item_desc}"
