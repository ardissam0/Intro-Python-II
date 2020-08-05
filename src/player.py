from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name 
        self.location = location 
        self.inventory = []

    def move(self, direction):
        if direction in ['n', 's', 'e', 'w']:
            move_location = self.location.get_directions(direction)
            if move_location is not None:
                self.location = move_location
                print(self.location)
            else:
                print("Can't move that way!")

    def toggle_inventory(self):
        print(f"{self.name}'s Inventory: ")
        for item in self.inventory:
            print(item)

    def add_item(self, item):
        item.take_it()
        self.inventory.append(item)

    def drop_item(self, item):
        item.drop_it()
        self.inventory.remove(item)
