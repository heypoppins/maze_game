import time
next_room = 1
def run_room():
      print("It's an especially foggy day as your carriage brings you to your new job as a guard. The carriage stops and you hand\n"
            "the driver his deserved pay. The prison is a dark, menacing building with one massive tower and massive wall surrounding it.\n"
            "At the top of the tower is the twirl of a fireball, meant to light the dungeon's surroundings.")

      input("\n\tPress ENTER to continue:")

      print("\nYou pass through the security station, whose guards question you and let you in. The inside of the prison is dimly lit and\n"
            "smells of mildew. You find the officer who is to give you your station. He walks you down a long hallway which has a gaurded door.\n"
            "The door itself is made of earth and is held together through suspension magic.")

      input("\n\tPress ENTER to continue:")

      print("\nThe officer tells the others to open up, the door crumbles into dust as you and the officer make your way into the barracks.\n"
            "In the barracks is your new squad, who you've met before. Each man has bags under his eyes and is looking down, only using\n"
            "their eyes to direct their attention. Some have massive, visible scars, while the others only have smaller scars or scars covered by\n"
            "by their armor.")

      input("\n\tPress ENTER to continue:")

      print("\nYou suit up and walk through the garrison, which is deathly silent as the only noise is the footsteps of your squad, the\n"
            "occasional drip of water, and the scurrying of rats. You make your way to another door, once again made of earth, but it has\n"
            "a tint of purple and a magical sheen covering it. The door slides away and within the dark and heavy room is a beam of light,\n"
            "still unable to penetrate the darkness. Chains come from the walls to leash a man on his ankles and hands with his back to you.")

      input("\n\tPress ENTER to continue:")

      print("\nThe shackles barely fit the man's wrist as he may have easily been able to slip out of them. The man himself is very old,\n"
            "on his chin are long gray strands that resemble a starved beard. The man's build is tiny, he has been starved so much his ribs\n"
            "potrude from his body more than his chin. 'I can feel it' he aches. 'It is coming... You cannot hold me.' The men all shudder\n"
            "and reach for their swords.")

      input("\n\tPress ENTER to continue:")

      print("\nThe officer gives a relieving wave with his hand commanding the group to relax. The officer walks up to the old man and they share a few\n"
            "whispered words. The door behind everyone begins to seal up and the officer gives a concerned look. The old man begins to shake\n"
            "shake and quiver.")

      input("\n\tPress ENTER to continue:")

      print("\nHe lets out a blood curdling scream as the white light turns red. His body enlarges and continues to grow as the door's magical tint\n"
            "turns from purple to deep red. Hair begins to potrude from his naked body and his hands turn to massive paws. The officer begins\n"
            "to jump away, but the creature whips it's neck towards him and with a new giant snout, chomps into the officer's neck. The\n"
            "officer screams and the men grab for their swords.")

      input("\n\tPress ENTER to continue:")

      print("\nThe new creature has black fur, sword-like claws on each finger and toe, a massive snout filled with dagger-sized teeth,\n"
            "and glowing red eyes. It stands tall enough that two men stacked on one another would still struggle to reach it's wolfish ears.")

      input("\n\tPress ENTER to continue:")

      print("\nA guard charges in as one backs up to load his crossbow. The monster swipes it's paws towards the guard and tears the man in half.\n"
            "It leaps to the others and stabs one in the thigh while biting off the chest off of another. You stand there frozen as the monster\n"
            "twirls and leaps, slashing through every guard that edges near it.")

      input("\n\tPress ENTER to continue:")

      print("\nThe creature's fur runs red with the blood of it's prey. It's glaring eyes meet yours as more guards foolishly seek the glory of killing\n"
            "the beast. A paw slams your chest and you fly to the wall behind you and hit your head on the door, rendering you unconscious, as the\n"
            "echoes of screams reverberate through the prison.")

      input("\n\tPress ENTER to continue to tutorial:")

      #Tutorial
      print("----------------------------------------------------------------")

      print("!  Tutorial  !")
      print('''
      Commands:
      
            Use 'go' to move about the dungeon.
            To use 'go' type 'go direction' with direction being 'north', 'south', 'east', and 'west'
      
            Use 'take' to add items from the room to your inventory
            To use 'take' type 'take item' with item being the thing you are trying to take
      
            Use 'drop' to remove items from your inventory and place them in the room
            To use 'drop' type 'drop item' with  item being the thing you are trying to drop
      
            Use 'use' to use an item to see if the item has an interaction within the room
            To use 'use' type 'use item'  with  item being the thing you are trying to use
            You can type 'use heal' if you have the heal spell to heal yourself, you can only do this once in each room
      
            Use 'status' to view either your player inventory or to view what is available for you to take within the room
            To use 'status' type 'status player' or 'status room' depending on what you wish to view
      
            Use 'loot' to take items from specific sources within the room (i.e. corpses, chests)
            To use 'loot' type 'loot' and a menu will pop up asking you to identify the source and then the item you wish to take
      
            Use 'equip' to determine which item you would like to use once in combat
            To use 'equip' type 'equip' and a menu will pop up asking whether you would like to equip Weapons or Spells then you
            will be asked to identify the item you would like to equip
      ''')
      input("Press ENTER to continue tutorial:")
      print('''
      Combat:
            Once you have engaged in combat, you will be prompted to either 'attack' or 'block'
            
            To 'attack' type 'attack' and you will be prompted to identify whether you want to attack with Weapons or Spells
            You will then attack the creature with whatever Weapon or Spell you have equipped
            If you do not have an item equipped, the game will prompt you to equip an item
            Keep in mind: You cannot heal in combat! So be careful!
            
            To 'block' type 'block' and you will prevent all damage from the monsters attack
            
            After you chose to 'attack' or 'block' the monster will attack you unless it is dead
      ''')

      input("Press ENTER to continue to the game:")
      print("Loading....")
      time.sleep(1)
      print("\n     *")
      time.sleep(1)
      print("    * *")
      time.sleep(1)
      print("    * *")
      time.sleep(1)
      print("    * *")
      time.sleep(1)
      print("    * *")
      time.sleep(1)
      print("   *****")
      time.sleep(1)
      print("     *")
      time.sleep(1)
      print("     *")
      time.sleep(1)
      print("----------------------------------------------------------------")
      print("\n\t\tYou awake to a loud howl.")


      return next_room