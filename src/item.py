class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description 

    def __repr__(self):
        return f"{self.name}, Description: {self.description}"

    def take_it(self):
        print(f"You picked up a{self.name}")

    def drop_it(self):
        print(f"You dropped a {self.name}")