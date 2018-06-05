import adventure_game.my_utils as utils

room8_inventory = {}

room8_status = {}

room8_map = '''
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

room8_loot_sources = 0
room_state = {
    'heal' : True,
    'is_locked' : True
}
# # # # # # # # #
#   Room 8
#
#   North: 10  East: 5  South: /  West: /
#
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    The room seems to look like an abandoned living space. There is an empty table in the center and a dusty study on the
    southern wall. There is a door to the north and a passage to the east.
    '''

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "loot", "equip"]
    no_args = ["loot", "equip"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 8

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            if direction == 'north':
                if room_state['is_locked']:
                    print('''
            You suddenly hear a faint voice whisper, 'You may not go further into my residence if you do not
            identify my being. I have no legs, yet I can dance. I have no lungs, yet I breathe. I have no life to lose,
            yet I am capable of dying.'
                        ''')
                    while True:
                        print("Type 'Q' if you wish to stop guessing.")
                        answer = input("What am I?\n")
                        answer = answer.title()
                        if answer == 'Q':
                            print("You are done guessing.\n")
                            break
                        elif answer == 'Fire':
                            print("The voice catches your ear, saying 'You may enter'.")
                            next_room = 10
                            room_state["is_locked"] = False
                            done_with_room = True
                            break
                        else:
                            print("The door does not move.\n")
                else:
                    print("The voice says, 'You may enter.'")
            elif direction == 'east':
                next_room = 5
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room8_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room8_inventory, room8_map, room8_loot_sources)
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
