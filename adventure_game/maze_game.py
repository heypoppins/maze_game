import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")
# room imports
import adventure_game.rooms.room1 as r1
import adventure_game.rooms.room2 as r2
import adventure_game.rooms.room3 as r3
import adventure_game.rooms.room4 as r4
import adventure_game.rooms.room5 as r5
import adventure_game.rooms.room6 as r6
import adventure_game.rooms.room7 as r7
import adventure_game.rooms.room8 as r8
import adventure_game.rooms.room9 as r9
import adventure_game.rooms.room10 as r10
import adventure_game.rooms.room11 as r11
import adventure_game.rooms.room12 as r12
import adventure_game.rooms.room13 as r13
import adventure_game.rooms.room14 as r14
import adventure_game.rooms.room15 as r15

import adventure_game.rooms.room0 as r0

# Default the player to the first room
room_number = 0

# Map:
#          *13*
#           |
#   10      11     12(?)    Legend:
#   |       |       |           # = Room
#   8 - 5 - 6 - 7 - 9           - and | = Available Paths
#       |   |   |               @ = Character Location
#       3 - 2 - 4
#           |
#           1

player_health = {
    'pl_hp' : 5
}

# Player Inventory
player_inventory = {
    'Iron Sword' : 1,
    'Steel Sword' : 0,
    'Officer Sword' : 0,
    'Silver Sword' : 0,
    'Mithril Sword' : 0,
    'Sword Of Burning' : 0,
    'Sword Of The Sacred-Light' : 0,
    'Heal' : 0,
    'Bolster' : 0,
    'Fireball' : 1,
    'Sacred-Light' : 0,
    'Blood-Let' : 0,
    'Torch': 1,
    'Key' : 0
}

player_equipped = {
    'Weapons' : {'Iron Sword' : 1,
        'Steel Sword' : 0,
        'Officer Sword' : 0,
        'Silver Sword' : 0,
        'Mithril Sword' : 0,
        'Sword Of Burning' : 0,
        'Sword Of The Sacred Light' : 0},
    'Spells' : {'Heal' : 0,
        'Bolster' : 0,
        'Fireball' : 1,
        'Sacred-Light' : 0,
        'Blood-Let' : 0}
}

#Weapons
combat_off_inventory = {
    "Iron Sword" : 1,
    "Steel Sword" : 2,
    "Officer Sword" : 4,
    "Silver Sword" : 5,
    "Mithril Sword" : 6,
    "Sword Of Burning" : 8,
    "Sword Of The Sacred Light" : 9
}

#Spells
combat_spell_inventory = {
    "Heal" : 2,
    "Bolster" : 4,
    "Fireball" : 3,
    "Sacred-Light" : 7,
    "Blood-Let" : 5
}

#Mobs = {"Name of Mob" : {Attack : Health}}
mobs = {
    "Young Wolf" : {'attack': 1, 'health' : 2},
    "Wolf" : {'attack': 3, 'health' : 4},
    "Feral Wolf" : {'attack' : 4, 'health' : 6},
    "Dire Wolf" : {'attack': 5, 'health' : 9},
    "Pack Alpha" : {'attack': 7, 'health' : 10},
    "Frightening Beast" : {'attack': 9, 'health' : 18}
}

print("\n\tWelcome to the Dungeon of the Claw!")
should_continue = True
while should_continue:
    if room_number == 15:
        room_number = r15.run_room
        print("GAME OVER")
        break
    elif room_number == 14:
        room_number = r14.run_room()
        break
    elif room_number == 0:
        room_number = r0.run_room()
    elif room_number == 1:
        room_number = r1.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 2:
        room_number = r2.run_room(player_inventory, player_equipped, player_health, combat_spell_inventory)
    elif room_number == 3:
        room_number = r3.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 4:
        room_number = r4.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 5:
        room_number = r5.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 6:
        room_number = r6.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 7:
        room_number = r7.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 8:
        room_number = r8.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 9:
        room_number = r9.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 10:
        room_number = r10.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 11:
        room_number = r11.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 12:
        room_number = r12.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)
    elif room_number == 13:
        room_number = r13.run_room(player_inventory, player_equipped, combat_off_inventory, combat_spell_inventory, mobs, player_health)

    else:
        print("Ack I don't know room number:", room_number)
        break
#

print("\nThe game has ended...")
