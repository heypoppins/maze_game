import adventure_game.my_utils as utils

room12_inventory = {}

room12_status = {}

room12_map = '''
Map:
     _______________
    |     ______    | 
    |    //¯¯¯¯\\\   |
    |    ¯     ||   |       Legend:       
    |        //     |           # = Room
    |       ||      |           - and | = Available Paths
    |        .      |           @ = Character Location
    |_______________|                    
'''

room12_loot_sources = {
    'Aura' : {"Sword Of The Sacred Light" : 1,
              "Sacred-Light" : 1}
}

# # # # # # # # #
#   Room 12
#
#   Secret Room!
#   North: /  East: /  South: 9  West: /
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    A glowing aura of blinding light floats in the center of the room. The aura hums and swirls, cascading light throughout
    the seemingly infinite room.
    '''
    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 3

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'south':
                next_room = 9
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room12_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room12_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room12_inventory, room12_map, room12_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            while True:
                print("The available loot sources are:\n")
                for key in room12_loot_sources.keys():
                    print("\t\t", key)
                chosen = input("\nWhich would you like to loot? Type 'Q' if you wish to stop looting.\n\t")
                chosen = chosen.title()
                if chosen == 'Q':
                    break
                elif chosen in room12_loot_sources:
                    utils.loot(chosen, room12_loot_sources, player_inventory)
                    break
                else:
                    print("That is not an available loot source.\n")
        elif the_command == 'use':
            interaction = response[1]
            if interaction == 'heal':
                print("A strange wind blows through the room and snuffs out the magic you are trying to use.")
        else:
            print("\n\tThat is not an available command in this room.\n\t")

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print("\n\tYou close you eyes and the light fades.\n\t")
        print("The torch you had placed has been burned up.")
    # end of main while loop
    return next_room
