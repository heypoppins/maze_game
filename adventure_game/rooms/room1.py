import adventure_game.my_utils as utils

# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  North: 1  East: /  South: /  West: /
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#   Use: There is nothing to use in this room

#
#Map:
#    _______
#   (       )       Legend:
#   (   #   )           # = Room
#   (   |   )           - and | = Available Paths
#   (   @   )           @ = Character Location
#   (_______)

#You press on the door and it slowly creaks ajar.
room1_status = {}

room1_map = '''
Map:
     _______________
    |               |
    |       #       |
    |       |       |       Legend:       
    |       @       |           # = Room
    |               |           - and | = Available Paths
    |               |           @ = Character Location
    |_______________|                    
'''
room1_inventory = {}

room1_loot_sources = {
    'Slashed Guard' : {'Steel Sword': 1},
    'Leaning Guard' : {'Heal': 1}
}

room_state = {
    'encounter' : True,
    'heal' : True
}
mob = 'Young Wolf'
rat_attack = 'The Young Wolf leaps towards you with a ferocious bite!'

def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = ("\nThe red light still shines in the dimly light room, exposing the gruesome scene of what used to"
                  "\nguards. To the west is a mossy wall stained with blood. To the east is a wall with guard's corpse"
                  "\npropped up against it. In the center are the torn shackles and another corpse. There's a passage going"
                  "\nnorth.\n")

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                if room_state['encounter']:
                    print("As you go to enter the next room, a Young Wolf attacks you!")
                    utils.combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob, player_health, rat_attack)
                    room_state['encounter'] = False
                    if player_health['pl_hp'] <= 0:
                        next_room = 15
                        done_with_room = True
                    else:
                        next_room = 2
                        done_with_room = True
                else:
                    next_room = 2
                    done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room1_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room1_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room1_inventory, room1_map, room1_loot_sources)
            else:
                print("That is not a valid option.")
        elif the_command == 'equip':
            utils.equip_item(player_equipped, player_inventory)
        elif the_command == 'loot':
            while True:
                print("The available loot sources are:\n")
                for key in room1_loot_sources.keys():
                    print("\t\t", key)
                chosen = input("\nWhich would you like to loot? Type 'Q' if you wish to stop looting.\n\t")
                chosen = chosen.title()
                if chosen == 'Q':
                    break
                elif chosen in room1_loot_sources:
                    utils.loot(chosen, room1_loot_sources, player_inventory)
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
                print("That is not an option in this room.")
        else:
            print("\n\tThat is not an available command in this room.\n\t")

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print("\n\tYou press on the door and it slowly creaks ajar.")
        print("********************************************************")
    # end of while loop
    return next_room
