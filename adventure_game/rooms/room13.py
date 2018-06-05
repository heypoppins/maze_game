import adventure_game.my_utils as utils

room13_inventory = {}

room13_status = {}

room13_map =  '''
Map:
     __________
    |           \     
    |            ¯_ 
    |   GOOD LUCK  |              
    |               \           
    |       X       |           
    |               |           
    |_______________|                    
'''

room13_loot_sources = {}

# # # # # # # # #
#   Room 13
#
#   Boss Fight!
#   North: /  East: /  South: (11)  West: /
#
#

mob = 'Frightening Beast'
beast_attack = "The Beast bears down on you with it's eyes and rips it's talons through your flesh."

def run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health):
    description = '''
    The room smells vile. A red mist permeates the air, making it difficult to see.The walls are covered in corpses of men 
    and animal and the ground is covered in blood. In the middle of the room lays the Beast. It rears it's hind legs and licks
    the blood off of it's talons. The Beast notices your presence and snarls.
    '''

    print(description)

    next_room = 13

    utils.combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob,
    player_health, beast_attack)
    if player_health['pl_hp'] <= 0:
        next_room = 15

    if player_health['pl_hp'] <= 0:
        print("A light consumes you...")
    else:
        print('''
            The corpse of the Beast slumps over and begins to shrink, losing it's fur and talons. The old man, once Beast, lays on
            the floor, slowly breathing, grasping his chest. Black blood pools around his as he quivers in agony. He looks up at you,
            standing over him, his eyes still red. He whispers 'Thank you.' and breathes his last breath.
            ''')

        input("\n\tPress ENTER to continue:")

        print('''
            All is quiet until...
            ''')

        input("\n\tPress ENTER to continue:")

        print('''
            The black blood of the man begins to shine a blinding white and light consumes you and knocks you to your knees. An 
            apparition of a young man approaches you through the light. He clasps your forearm and lifts you off the ground.
            He places both hands on your shoulders and the light begins to dissipate.
            ''')

        input("\n\tPress ENTER to continue:")

        print('''
        As you return to the room where the old man lie. An explosion of light blasts the northern wall down and guards flood
        into the dungeon. You collapse to the ground as your fellow prison guards run to aid you. The last thing you see is
        the young man in the light kneeling beside the old man, smiling solemnly.
        ''')
        next_room = 14
    # end of main while loop
    return next_room
