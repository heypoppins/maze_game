import adventure_game.my_utils as utils

room3_inventory = {}

room3_status = {}

room3_map = '''
Map:
     _______________
    |               | 
    |       #       |
    |       |       |       Legend:       
    |       @ - #   |           # = Room
    |               |           - and | = Available Paths
    |               |           @ = Character Location
    |_______________|                    
'''

room3_loot_sources = {
    'Statue' : {'Silver Sword' : 1}
}
room_state = {
    'heal' : True
}

# # # # # # # # #
#   Room 3
#
#   North: 5  East: 2  South: /  West: /
#
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    In the middle of the room is an ancient statue depicting a man with a sword fending off three wolves. The sword the warrior
    is holding is not cement like the statue, instead it looks like it's made of metal and has a realistic sheen. The warrior
    has an insignia on his arm saying 'Protector of the Flame'. There are passages going north and east.
    '''

    next_room = 3
    done_with_room = False


    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'north':
                next_room = 5
                done_with_room = True
            elif direction == 'east':
                next_room = 2
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room3_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room3_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room3_inventory, room3_map, room3_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            while True:
                print("The available loot sources are:\n")
                for key in room3_loot_sources.keys():
                    print("\t\t", key)
                chosen = input("\nWhich would you like to loot? Type 'Q' if you wish to stop looting.\n\t")
                chosen = chosen.title()
                if chosen == 'Q':
                    break
                elif chosen in room3_loot_sources:
                    utils.loot(chosen, room3_loot_sources, player_inventory)
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

