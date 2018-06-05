import adventure_game.my_utils as utils

room7_inventory = {}

room7_status = {}

room7_map = '''
Map:
     _______________
    |               | 
    |               |
    |               |       Legend:       
    |   # - @ - #   |           # = Room
    |       |       |           - and | = Available Paths
    |       #       |           @ = Character Location
    |_______________|                    
'''

room7_loot_sources = {
    'Bookcase' : {'Bolster' : 1}
}
room_state = {
    'heal' : True
}
# # # # # # # # #
#   Room 7
#
#   North: /  East: 9  South: 4  West: 6
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    The northern wall has a bookcase covering it. The bookcase is filled with cobwebs and only contains one book.
    There are passages going east, south, and west. 
    '''

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 7

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'east':
                next_room = 9
                done_with_room = True
            elif direction == 'south':
                next_room = 4
                done_with_room = True
            elif direction == 'west':
                next_room = 6
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room7_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room7_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room7_inventory, room7_map, room7_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            while True:
                print("The available loot sources are:\n")
                for key in room7_loot_sources.keys():
                    print("\t\t", key)
                chosen = input("\nWhich would you like to loot? Type 'Q' if you wish to stop looting.\n\t")
                chosen = chosen.title()
                if chosen == 'Q':
                    break
                elif chosen in room7_loot_sources:
                    utils.loot(chosen, room7_loot_sources, player_inventory)
                    break
                else:
                    print("That is not an available loot source.\n")
        elif the_command == 'use':
            interaction = response[1]
            if interaction == 'heal':
                if room_state['heal']:
                    if utils.has_a(player_inventory, 'Bolster'):
                        utils.heal(player_health, player_inventory, combat_spell_inventory)
                        room_state['heal'] = False
                    elif utils.has_a(player_inventory, 'Heal'):
                        utils.heal(player_health, player_inventory, combat_spell_inventory)
                        room_state['heal'] = False
                    else:
                        print("You do not have the heal spell!")
                else:
                    print("You have already used your heal in this room!\n")
        else:
            print("\n\tThat is not an available command in this room.\n\t")

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print("\n\tYou press on the door and it slowly creaks ajar.")
        print("********************************************************\n")
    # end of main while loop
    return next_room
