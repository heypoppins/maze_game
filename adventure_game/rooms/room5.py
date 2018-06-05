import adventure_game.my_utils as utils

room5_inventory = {}

room5_status = {}

room5_map = '''
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

room5_loot_sources = 0

room_state = {
    'heal' : True,
    'encounter' : True
}


# # # # # # # # #
#   Room 5
#
#   North: /  East: 6  South: 3  West: 8
#
#
#

mob = 'Feral Wolf'
wolf_attack = "The Wolf snarls and viciously snaps at you with it's strong jaws."

def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    The ground is damp from the drool of the wolf and the walls contain scratches. The red light still persists throughout the room.
    There are passages going east, south, and west.
    '''
    next_room = 5
    done_with_room = False

    if room_state['encounter']:
        print("In the middle of the stands a snarling wolf with deep red eyes and brown fur. You get a chance to look around the room.")
        print(description)
        utils.combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob,
                     player_health, wolf_attack)
        room_state['encounter'] = False
        if player_health['pl_hp'] <= 0:
            next_room = 15
            done_with_room = True
    else:
        print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'west':
                next_room = 8
                done_with_room = True
            elif direction == 'east':
                next_room = 6
                done_with_room = True
            elif direction == 'south':
                next_room = 3
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room5_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room5_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room5_inventory, room5_map, room5_loot_sources)
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
