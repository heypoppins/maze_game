import adventure_game.my_utils as utils

room9_inventory = {}

room9_status = {}

room9_map = '''
Map:
     _______________
    |               | 
    |               |
    |               |       Legend:       
    |   # - @       |           # = Room
    |               |           - and | = Available Paths
    |               |           @ = Character Location
    |_______________|                    
'''

room9_loot_sources = 0
room_state = {
    'heal' : True,
    'encounter' : True,
    'is_locked': True
}
# # # # # # # # #
#   Room 9
#
#   North: 11(?)  East: /  South: /  West: 7
#
#
#

mob = 'Dire Wolf'
alpha_attack = 'The wolf lashes out and claws at you.'

def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    On the western wall there is a painting of a man neatly dressed, giving the impression of a baron or a bishop. Upon closer
    inspection you see the man has the paws of a wolf and his eyes are a dark red. On the northern wall is an empty torch
    sconce. There is a passage going west.
    '''

    next_room = 9
    done_with_room = False

    if room_state['encounter']:
        print("You walk into the room and see a grimacing wolf with beaming red eyes staring you down. The wolf has jet black"
              "fur and massive talons.")
        utils.combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob,
                     player_health, alpha_attack)
        room_state['encounter'] = False
        if player_health['pl_hp'] <= 0:
            next_room = 15
            done_with_room = True
        else:
            print(description)

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
                next_room = 7
                done_with_room = True
            else:
                print("\n\tYou may not go in that direction.\n\t")
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room9_inventory, drop_what)
        elif the_command == 'status':
            status = response[1]
            if status == 'player':
                utils.player_status(player_inventory, player_equipped, player_health)
            elif status == 'room':
                utils.room_status(room9_inventory, room9_map, room9_loot_sources)
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
            if interaction == 'torch':
                if room_state['is_locked']:
                    if utils.has_a(player_inventory, 'Torch'):
                        print("You place the torch inside the sconce and the wall behind it shakes. A blinding light consumes you"
                              "and carries you into a new passage.")
                        player_inventory['Torch'] = player_inventory['Torch'] - 1
                        next_room = 12
                        done_with_room = True
                    else:
                        print("You do not possess a torch!.\n")
                else:
                    print("You are once again consumed by the light.")
        else:
            print("\n\tThat is not an available command in this room.\n\t")

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print("\n\tYou press on the door and it slowly creaks ajar.")
        print("********************************************************\n")
    # end of main while loop
    return next_room
