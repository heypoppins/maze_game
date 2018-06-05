import adventure_game.my_utils as utils

room11_inventory = {
    'Key' : 1
}

room11_status = {}

room11_map = '''
Map:
     _______________
    |               | 
    |       X       |
    |       |       |       Legend:       
    |       @       |           # = Room
    |       |       |           - and | = Available Paths
    |       #       |           @ = Character Location
    |_______________|                    
'''

room11_loot_sources = 0
room_state = {
    'heal' : True,
    'is_locked' : True,
    'encounter' : True
}
mob = 'Pack Alpha'
wolf_attack = "The Wolf leaps towards you and clamps down on your flesh."

# # # # # # # # #
#   Room 11
#
#   North: 13  East: /  South: 6  West: /
#
#


def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    There are skeletons of small animals covering the ground. On the northern wall is gate with a massive bloody paw print
    covering what seems to be a keyhole. There are passages to the north and to the south.
    '''

    next_room = 11
    done_with_room = False

    print(description)

    if room_state['encounter']:
        print("Amongst the bones in the room stands a massive wolf with many scars covering it's face. It's beaming eyes"
              "match the same tint of red as the blood on it's claws. Around it's neck is a rope with a key on it.")
        utils.combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob,
                     player_health, wolf_attack)
        room_state['encounter'] = False
        if player_health['pl_hp'] <= 0:
            next_room = 15
            done_with_room = True
        else:
            utils.take_item(player_inventory, room11_inventory, 'Key')

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
            if direction == 'north':
                if room_state['is_locked']:
                    print("The door is locked.")
                else:
                    print("You enter the room.")
                    next_room = 13
                    done_with_room = True
            elif direction == 'south':
                next_room = 6
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room11_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room11_inventory, room11_map, room11_loot_sources)
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
            if interaction == 'key':
                if utils.has_a(player_inventory, 'Key'):
                    if room_state['is_locked']:
                        print("You place the key into the keyhole and turn it until it clicks.\n")
                        room_state['is_locked'] = False
                        while True:
                            answer = input("Would you like to enter?")
                            answer = answer.title()
                            if answer == 'Yes':
                                next_room = 13
                                done_with_room = True
                                break
                            elif answer == 'No':
                                print("You back away from the room with the door still unlocked.")
                                break
                            else:
                                print("That is not a valid response.\n")
        else:
            print("\n\tThat is not an available command in this room.\n\t")

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print("\n\tYou press on the door and it slowly creaks ajar.")
        print("********************************************************\n")
    # end of main while loop
    return next_room
