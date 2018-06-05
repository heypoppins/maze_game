import adventure_game.my_utils as utils

room2_inventory = {
}

room2_status = {}

room2_map = '''
Map:
     _______________
    |               | 
    |       #       |
    |       |       |       Legend:       
    |   # - @ - #   |           # = Room
    |       |       |           - and | = Available Paths
    |       #       |           @ = Character Location
    |_______________|                    
'''
room2_loot_sources = 0
room_state = {
    'heal' : True
}

# # # # # # # # #
#   Room 2
#
#   North: 6  East: 4  South: 1  West: 3
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop.

def run_room(player_inventory, player_equipped, player_health, combat_spell_inventory):

    description = '''
    A red light persists throughout the room and shines down on an blood trail going north. There is a faint drip of water 
    coming from the ceiling. There are passages going north, east, south, and west.
    '''
    player_hp = utils.get_player_hp(player_health)
    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 2

    done_with_room = False
    if player_hp == 0:
        next_room = 15
        done_with_room = True
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'east':
                next_room = 4
                done_with_room = True
            elif direction == 'west':
                next_room = 3
                done_with_room = True
            elif direction == 'north':
                next_room = 6
                done_with_room = True
            elif direction == 'south':
                next_room = 1
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room2_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room2_inventory, room2_map, room2_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            print("There are no loot sources in this room.")
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
