import adventure_game.my_utils as utils

room4_inventory = {
    'Blood-Let' : 1
}

room4_status = {}

room4_map = '''
Map:
     _______________
    |               | 
    |       #       |
    |       |       |       Legend:       
    |   # - @       |           # = Room
    |               |           - and | = Available Paths
    |               |           @ = Character Location
    |_______________|                    
'''

room_state = {
    'heal' : True
}
room4_loot_sources = 0

# # # # # # # # #
#   Room 4
#
#   North: 7  East: /  South: /  West: 2
#
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    In the middle of the room is a fountain of blood. The fountain is elegantly designed with etchings of ancient battles
    between man and wolf.  The dark red light of the room fades into a ruby shade towards the middle of the room. There are
    passages going north and west.
    '''
    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 4

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'north':
                next_room = 7
                done_with_room = True
            elif direction == 'west':
                next_room = 2
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room4_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room4_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room4_inventory, room4_map, room4_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            print("There is nothing to loot in this room.")
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
