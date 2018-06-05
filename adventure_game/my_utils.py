import random
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#   valid_options : A list of string values you expect your user to respond with.
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False;
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result

# END ask_command

def has_a(player_inventory, item):
    if item in player_inventory.keys():
        count = player_inventory[item]
        if count > 0:
            return True
        else:
            return False
    else:
        return False

#end of has_a

def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        current_count = player_inventory[item]
        player_inventory[item] = current_count - 1
        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count + 1
        else:
            room_inventory[item] = 1
        print("You dropped the", item)
    else:
        print("You cannot drop what you do not possess.")

#end of drop_item

def take_item(player_inventory, room_inventory, item):
    item = item.title()
    if has_a(room_inventory, item):
        room_count = room_inventory[item]
        room_inventory[item] = room_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
        print("You have taken:", item, "\n")
    else:
        print("There is no", item, "in this room.")

#end of take_item

def room_status(room_inventory, map, loot):
    print("\tIn the room you see:")
    nothing = True
    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            nothing = False
            print("\t\t", key)
    print("\n")
    if nothing == True:
        print("\t...sadly, nothing to take.\n")
    print("Location of Room:", map, "\n")
    print("In the room there are the available loot sources:\n")
    if loot == 0:
        print("\t...sadly, nothing to loot.\n")
    else:
        for key in loot:
            print("\t\t", key)
        print("\n")


#end of room_status

def player_status(player_inventory, player_equipped, player_health):
    player_hp = get_player_hp(player_health)
    print("\n\tYour health is currently:", player_hp, "\n")
    print("\tYou are in possession of:\n")
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print("\t\t",key, ' : ', player_inventory[key])
    print("\n")
    print("\tYou have equipped:")
    for dictn in player_equipped.keys():
        stuff = player_equipped[dictn]
        print("\n\t\tEquipped in", dictn, ":")
        for key in stuff:
            if stuff[key] > 0:
                print("\t\t", key, ' : ', stuff[key])
    print("\n")


#end of player_status

###############################
#
#   player_equipped is the full list of item sectioned by 'Weapons' and 'Spells'
#   edit is the player's choice of if they want to select weps or spells to edit
#   equip_inv is dictionary of weps or spells, used to separate the dicts of pl_equipped and 'Weps' or 'Spells'
#   inv_dict and equip_dict are the player_inventory and player_equipped without items the player doesnt possess
#   possible_to should be all the items in the player_inventory you are able to equip
#   equipped is what you currently have equipped
#

def equip_item(player_equipped, player_inventory):
    while True:
        edit = input("Would you like to edit 'Weapons' or 'Spells'?: ")
        edit = edit.title()
        if edit == 'Q':
            print("You are done equipping.")
            break
        elif edit in player_equipped:
            equip_inv = player_equipped[edit]
            while True:
                equipped = equip_without(equip_inv)

                equip_str = str(equipped)
                equip_str = equip_str.strip("{")
                equip_str = equip_str.strip("}")
                equip_str = equip_str.strip(": 1")

                print("Your equipped in", edit, ":", equip_str)
                pos = equip_inv
                possible_to = inv_without(player_inventory)

                pos_str = str(possible_to)
                pos_str = pos_str.strip("[")
                pos_str = pos_str.strip("]")
                print("Your inventory:", pos_str,"\n")

                item = input("What item would you like to equip? Type 'Q' to quit equipping.")
                item = item.title()
                if item in possible_to:
                    if item in pos:
                        if item == 'Heal':
                            print("You are unable to equip: 'Heal' (Hint: you don't have to equip Heal to use it!)\n")
                        if item == 'Bolster':
                            print("You are unable to equip: 'Bolster' (Hint: you don't have to equip Bolster to use it!)\n")
                        else:
                            for key in equip_inv:
                                equip_inv[key] = 0
                            equip_inv[item] = 1
                            player_equipped[edit] = equip_inv
                            print("\nYou have equipped: ", item)
                    else:
                        print("That item is not in ", edit)
                elif item == 'Q':
                    print("\n")
                    action = input("Type 'Q' if you wish to be fully done with equipping. If you would like to continue, press ENTER.\n")
                    action = action.title()
                    if action == 'Q':
                        return player_equipped
                    else:
                        break
                else:
                    print("Unable to equip:", item, "as you may not have the item or it may not exist.\n")
        else:
            print("That is not a type of item available for you to equip.\n")
    return player_equipped

#def get_possible_to(player_inventory, edit):

#end of equip

def inv_without(player_inventory):
    inv_dict = []
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            inv_dict.append(key)
    return inv_dict

def equip_without(inv):
    equip_dict = {}
    #equip_type is weapons or spells
    for key in inv.keys():
        if inv[key] > 0:
            equip_dict[key] = inv[key]
    return equip_dict

#end of equip_item

####################################################################
#
#   chosen is a string the user supplied, e.g. 'Slashed Guard'
#   source = {
#       'Slashed Guard' : {'Iron Sword': 2},
#       'Leaning Guard' : {'Crossbow': 1,
#                       'Iron Bolts': 1}
#       }
#
def loot(chosen, source, player_inventory):
    while True:
        if chosen in source:
            source_inventory = source[chosen]
            print("In loot source:", chosen, "these items are available:", source_inventory)
            item = input("\n\tWhat item would you like to loot? Type 'Q' if you are done looting.\n\t")
            item = item.title()
            if item == 'Q':
                print("You are done looting\n")
                break
            elif item in source_inventory:
                loot_take(player_inventory, source_inventory, item)
            else:
                print("That item is not in:", chosen, "\n")
    else:
        print("That is not a loot source.")

#end of loot

def loot_take(player_inventory, source_inventory, item):
    if has_a(source_inventory, item):
        source_count = source_inventory[item]
        source_inventory[item] = source_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
        print("You have taken:", item)
    else:
        print("There is no", item, "on this source.")

#end of loot_take

def scrub_response( dirty_response ):
    result = []
    result.append(dirty_response[0])
    if len(dirty_response) > 1:
        argument = dirty_response[1]
        if argument == 'short':
            result.append('short sword')
        elif argument == 'ice':
            result.append('ice pick')
        else:
            result.append(argument)

#end of scrub_response

    return result


def get_mob_at(mob, mobs):
    mob_stats = mobs[mob]
    mob_at = mob_stats['attack']
    return mob_at

def get_mob_hp(mob, mobs):
    mob_stats = mobs[mob]
    mob_hp = mob_stats['health']
    return mob_hp

def get_weapon_stats(combat_off_inventory, wep):
    wep_att = combat_off_inventory[wep]
    return wep_att

def get_spell_stats(combat_spell_inventory, spell):
    spell_att = combat_spell_inventory[spell]
    return spell_att

def mob_status(hp, max):
    if hp <= 0:
        status = "dead!\n"
        return status
    elif hp < (max/5):
        # if hp < 20%
        status = "heavily wounded and on its last leg.\n"
        return status
    elif hp < (max/3):
        # if hp < 30%
        status = "wounded, but still willing to fight.\n"
        return status
    elif hp < (max/2):
        # if hp < 50%
        status = "hurting, the damage is starting to take its toll.\n"
        return status
    elif hp < (max/1.5):
        # if hp < 66%
        status = "hurting, but still capable to put up a good fight.\n"
        return status
    elif hp < (max/1.25):
        # if hp < 80%
        status = "bruised but beginning to feel more pain.\n"
        return status
    elif hp < (max/1.1):
        # if hp < 90%
        status = "shaken and teeming with rage.\n"
        return status
    else:
        status = "healthy and angry.\n"
        return status
#end of mob_status


def combat(player_equipped, player_inventory, combat_off_inventory, combat_spell_inventory, mobs, mob, player_health, mon_att):
    attack = get_mob_at(mob, mobs)
    attack = int(attack)
    hp = get_mob_hp(mob, mobs)
    hp = float(hp)
    print("!  You entered combat with:", mob, "!")
    while True:
        max_hp = get_mob_hp(mob, mobs)
        max_hp = float(max_hp)
        action = input("\nWould you like to attack or block?\n")
        action = action.lower()
        if action == 'block':
            print("You blocked the attack of:", mob, "\n")
        elif action == 'attack':
            mob_com = True
            while mob_com:
                tool = input("Would you like to attack with a Weapon or use a Spell?\n")
                tool = tool.title()
                if tool == 'Weapon':
                    wep = equip_without(player_equipped['Weapons'])
                    for key in wep:
                        wep = str(key)
                    if wep == {}:
                        print("You must equip an item:\n")
                        equip_item(player_equipped, player_inventory)
                        input("Press ENTER to resume combat\n")
                        wep = equip_without(player_equipped['Weapons'])
                        for key in wep:
                            wep = str(key)
                    att = get_weapon_stats(combat_off_inventory, wep)
                    att = int(att)
                    print("You attacked the", mob, "with", wep)
                    mob_com = False
                elif tool == 'Spell':
                    spell = equip_without(player_equipped['Spells'])
                    for key in spell:
                        spell = str(key)
                    if spell == {}:
                        print("You must equip an item:\n")
                        equip_item(player_equipped, player_inventory)
                        input("Press ENTER to resume combat\n")
                        spell = equip_without(player_equipped['Spells'])
                        for key in spell:
                            spell = str(key)
                    elif spell == "Heal":
                        print("You cannot heal in combat! You must equip another spell.")
                        equip_item(player_equipped, player_inventory)
                        input("Press ENTER to resume combat\n")
                        spell = equip_without(player_equipped['Spells'])
                        for key in spell:
                            spell = str(key)
                    elif spell == "Bolster":
                        print("You cannot heal in combat! You must equip another spell.")
                        equip_item(player_equipped, player_inventory)
                        input("Press ENTER to resume combat\n")
                        spell = equip_without(player_equipped['Spells'])
                        for key in spell:
                            spell = str(key)
                    else:
                        print("")
                    att = get_spell_stats(combat_spell_inventory, spell)
                    att = int(att)
                    print("You cast", spell, "on", mob)
                    mob_com = False
                else:
                    print("That is not an option.")
            hp = hp - att
            if hp <= 0:
                print("!  You beat", mob, "in combat  !\n")
                break
            status = mob_status(hp, max_hp)
            hit = random.randint(0, attack)
            hit = hit * -1
            update_hp(player_health, hit)
            if player_health['pl_hp'] <= 0:
                print(mon_att)
                break
            if hit == 0:
                print("The", mob, "has missed it's attack!")
            else:
                print(mon_att)
            print("\n")
            print("Your health is currently:", player_health['pl_hp'])
            print("The", mob, "is", status)
        else:
            print("That is not an option.")
    return player_health


def get_player_hp(player_health):
    player_hp = player_health['pl_hp']
    return player_hp

def heal(player_health, player_inventory, combat_spell_inventory):
    if has_a(player_inventory, 'Bolster'):
        change = get_spell_stats(combat_spell_inventory, 'Bolster')
        update_hp(player_health, change)
    elif has_a(player_inventory, 'Heal'):
        change = get_spell_stats(combat_spell_inventory, 'Heal')
        update_hp(player_health, change)
    else:
        print("You do not have a heal spell!")
    print("You have healed yourself! You now have", player_health['pl_hp'], "health.\n")



def update_hp(player_health, change):
    player_hp = player_health['pl_hp']
    player_hp = player_hp + change
    player_health['pl_hp'] = player_hp
    return player_health