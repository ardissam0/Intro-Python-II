from room import Room
from player import Player
from item import Item 
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

player = Player("Sam", room['outside'])

stick = Item("Stick", "A fallen branch.")
meat = Item("Meat", "Grab something to eat")
axe = Item("Axe", "A rusty axe from an old battle")
sword = Item("Sword", "A finely crafted sword")
gold = Item("Gold", "Coins to buy other items")
scroll = Item("Scroll", "Ancient writings, may be worth something")

room["outside"].items.append(stick)
room["outside"].items.append(axe)
room["foyer"].items.append(sword)
room["overlook"].items.append(scroll)
room["overlook"].items.append(sword)
room["narrow"].items.append(meat)
room["treasure"].items.append(gold)


# Write a loop that:

directions = ['n', 's', 'e', 'w']

# * Prints the current room name
print(player.location)

while True:
    command = input("Enter valid input: ")
    if command in directions:
        player.move(command)

    elif command == 'inv':
        player.toggle_inventory()

    elif command == 'grab stick':
        player.add_item(stick)
        player.location.take_item(stick)

    elif command == 'drop stick':
        player.drop_item(stick)
        player.location.add_items(stick)

    elif command == 'grab axe':
        player.add_item(axe)
        player.location.take_item(axe)

    elif command == 'drop axe':
        player.drop_item(axe)
        player.location.add_items(axe)

    elif command == 'grab sword':
        player.add_item(sword)
        player.location.take_item(sword)

    elif command == 'drop sword':
        player.drop_item(sword)
        player.location.add_items(sword)

    elif command == 'grab meat':
        player.add_item(meat)
        player.location.take_item(meat)

    elif command == 'drop meat':
        player.drop_item(meat)
        player.location.add_items(meat)

    elif command == 'grab gold':
        player.add_item(gold)
        player.location.take_item(gold)

    elif command == 'drop gold':
        player.drop_item(gold)
        player.location.add_items(gold)

    elif command == 'grab scroll':
        player.add_item(scroll)
        player.location.take_item(scroll)

    elif command == 'drop scroll':
        player.drop_item(scroll)
        player.location.add_items(scroll)
    
    elif command == 'q':
        print("Goodbye for now!")
        break

    else:
        print("Error, Choose valid input!")
    
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
