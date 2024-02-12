import random


class AdventureGame:
    def __init__(self):
        self.goggles_on = False
        self.torch_on = False
        self.flaming_sword = False
        self.HP = 3
        self.dwarf_king_HP = 5
        self.dogs_dead = False
        self.key = 0
        self.treasure = 0
        self.dog_time_limit = 3
        self.dwarf_time_limit = 6
        self.dwarf_king_dead = False
        self.found_pillar_key = False
        self.found_pillar_potion = False
        self.found_WC_key = False
        self.stone_unlocked = False
        self.stone_pilfered = False
        self.vault_locked = True
        self.stone_sword_HP = 3
        self.troglodyte_HP = 3
        self.check_peed = False

    def get_valid_input(self, prompt, valid_responses):
        print_prompt = True
        while True:
            if print_prompt:
                user_input = input(prompt).strip().upper()
                print_prompt = False
            else:
                user_input = input().strip().upper()

            if user_input in valid_responses:
                return user_input
            else:
                print("Invalid input. Please try again.")

    def restart_game(self):
        print("Game restarting...")
        self.goggles_on = False
        self.torch_on = False
        self.flaming_sword = False
        self.HP = 3
        self.dwarf_king_HP = 5
        self.dogs_dead = False
        self.key = 0
        self.treasure = 0
        self.dog_time_limit = 3
        self.dwarf_time_limit = 6
        self.dwarf_king_dead = False
        self.found_pillar_key = False
        self.found_pillar_potion = False
        self.found_WC_key = False
        self.stone_unlocked = False
        self.stone_pilfered = False
        self.vault_locked = True
        self.stone_sword_HP = 3
        self.troglodyte_HP = 3
        self.check_peed = False
        self.start_game()

    def start_game(self):
        print(r"  _________ __                         ____  __.__            /\        .____           .__        ")
        print(r" /   ______/  |_ ____   ____   ____   |    |/ _|__| ____   ___)/ ______ |    |   _____  |_________ ")
        print(r" \_____  \\   __/  _ \ /    \_/ __ \  |      < |  |/    \ / ___\/  ___/ |    |   \__  \ |  \_  __ \ ")
        print(r" /        \|  |(  <_> |   |  \  ___/  |    |  \|  |   |  / /_/  \___ \  |    |___ / __ \|  ||  | \/")
        print(r"/_______  /|__| \____/|___|  /\___  > |____|__ |__|___|  \___  /____  > |_______ (____  |__||__|   ")
        print(r"        \/                 \/     \/          \/       \/_____/     \/          \/    \/           ")

        print("\n\nYour mission is to plunder as much treasure as you can,"
              "and escape the stone king's lair alive!.\n\n")
        self.question1()

    def you_escaped(self):
        print("You open the hatch, and see a long vertical tunnel with hundreds of ladder rungs inside.\n"
              "You begin to climb up, one rung at a time. Eventually, you come to another hatch above you.\n"
              "You open this hatch and are blinded by the light of day! You have reached the surface!\n\n"
              "You have escaped the stone dwarf king's lair!\n\n")
        print(f"You collected {self.treasure}/23 treasures while in the lair.\n\n"
              f"You win!")
        self.prompt_restart()

    def question3(self):
        question_text = ("You look over the edge of the chasm. You see a pool of water, thirty feet below.\n\n"
                         
                         "A: Jump down into the chasm - heedless of the potential danger! There could be treasure!\n"
                         "B: Turn back to the door.\n\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response == "A":
            if self.torch_on:
                print("Your torch sputters and dies, plunging you into darkness! You quickly strap on your dark-vision "
                      "goggles!\n")
                self.torch_on = False
            self.question_chasm_1()
        elif response == "B":
            self.question2_2()

    def question_chasm_1(self):
        question_text = ("You leap from the precipice down into the cold cavern pool with a splash!\n"
                         "As you come up for air, you splutter and flail for a moment - the water is frigid!\n"
                         "Wading at the surface, you see a shoreline that leads into a naturally formed cave.\n"
                         "There is also a faint glimmer deep under the water.\n\n"

                         "A: Swim to the shoreline.\n"
                         "B: Try to dive down for the glimmering object.\n\n")

        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            self.question_chasm_shore_1()

        if response.upper() == "B":
            self.question_chasm_2()

    def question_chasm_2(self):
        question_text = ("You take a deep breath and dive down into the water. With your goggles on, you can see the\n"
                         "object you seek is an ornate sword, caught under a large boulder!\n\n"

                         "A: Try to unseat the sword from it's place - pinned between boulders.\n"
                         "B: Go back up for air.\n\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            self.question_chasm_dive()

        if response.upper() == "B":
            print("You go back up for air. Gods, this water is icy! You take one wound as hypothermia begins to set in."
                  "\n\n")
            self.HP -= 1
            self.check_HP()
            print(f"Current HP: {self.HP}\n\n")
            self.question_chasm_2_1()

    def question_chasm_2_1(self):
        question_text = ("You are once again treading water on the surface of the pool.\n\n"
                         "A: Dive back down for that sword.\n"
                         "B: Swim to shore.\n\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            self.question_chasm_dive()

        if response.upper() == "B":
            self.question_chasm_shore_1()

    def question_chasm_dive(self):
        print("You dive deeper still, and find yourself at the bottom of the pool. You grasp the hilt of the blade!\n"
              "you plant your feet on the rocky pond floor and pull!\n")

        while self.HP > 0 and self.stone_sword_HP > 0:
            roll_result = random.random()
            if roll_result <= 0.8:
                print("You succeed in pulling the stone a little farther out! You keep pulling.\n")
                self.stone_sword_HP -= 1
            else:
                print("You fail to pull the sword any farther out and begin drowning!\n"
                      "You lose 1 HP!\n"
                      "You keep trying!\n")
                self.HP -= 1

            if self.stone_sword_HP <= 0:
                print("You heave against the sword a final time, and you succeed in yanking it out!\n"
                      "You triumphantly swim to shore, and as you leave the pool, the sword bursts into flame!\n\n"
                      "You have received: +2 Flaming Sword\n\n")
                self.flaming_sword = True
                break

            if self.HP <= 0:
                print("You fail to pull the sword out in time, and drown!\n"
                      "You died!\n\n")
                self.prompt_restart()
                break

        self.question_chasm_shore_1()

    def question_chasm_shore_1(self):
        question_text = ("Finding yourself on the shoreline, you take a look around and see there is a large\n"
                         "passage that leads deeper into the cavern. The passage ascends and curves to the right\n"
                         "as you go. You reach the end of the winding path and find the cavern opens into a small\n"
                         "cavernous room with a tiny campfire in its center. Three troglodytes stand from their\n"
                         "seated places by the fire as you enter the room. They bellow and howl, raising clubs!\n\n"
                         
                         "A: Fight the troglodytes!\n"
                         "B: Try to frighten the beast-men away.\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response == "A":
            self.question_chasm_trog_fight()
        elif response == "B":
            self.question_chasm_trog_reason()

    def question_chasm_trog_reason(self):
        roll_result = random.random()
        if roll_result <= 0.8:
            print("Intimidation Success: 'Back! Away!' You shout at the troglodytes flagging about in a\n"
                  "menacing way. The beasts shy away, giving you a wide berth. They push a small boulder against the\n"
                  "back wall away, and escape down a small tunnel.\n"
                  "You look about the cave and find a desiccated corpse.\n"
                  "It is wearing a fine silver necklace, and has several jeweled rings!\n\n")
            self.treasure += 4
            print(f"You have found {self.treasure} treasures so far.\n\n")

            print("You follow down the tunnel, and discover path that leads to a stone corridor.\n")
            self.question3_torch_1()
        else:
            print("Intimidation Failure: The troglodytes hoot and holler all the louder, and charge you!")
            self.question_chasm_trog_fight()

    def question_chasm_trog_fight(self):

        verbs = ["clobber", "smack", "wail on", "beat"]
        print("You and the troglodytes begin an epic battle!")

        while self.HP > 0 and self.troglodyte_HP > 0:
            # Player attacks troglodytes
            if self.flaming_sword:
                if random.random() <= 0.8:
                    attack_verb = random.choice(verbs)
                    self.troglodyte_HP -= 1
                    print(f"You {attack_verb} the troglodytes with your flaming sword, killing one dead!"
                          f" Troglodytes left:", self.troglodyte_HP)
                else:
                    print("You miss the troglodytes!")

            if not self.torch_on and not self.flaming_sword:
                if random.random() <= 0.4:
                    attack_verb = random.choice(verbs)
                    self.troglodyte_HP -= 1
                    print(f"You {attack_verb} the troglodytes with your bare hands, killing one dead!"
                          f" Troglodytes left:", self.troglodyte_HP)
                else:
                    print("You miss the troglodytes!")

            # Check if troglodytes are is defeated
            if self.troglodyte_HP <= 0:
                print("Congratulations! You defeated the troglodytes!")
                break

            # troglodytes attack the player
            if random.random() < 0.5:
                attack_verb = random.choice(verbs)
                self.HP -= 1
                print(f"The troglodytes {attack_verb} you with their clubs! Your HP:", self.HP)
            else:
                print("The troglodytes fail to hurt you!")

            # Check if player is defeated
            if self.HP <= 0:
                print("You were defeated by the troglodytes. Game Over!")
                self.prompt_restart()
                break

        print("The battle has ended, and you are victorious!\n\n"
              "You look about the room and notice a few things: you find a desiccated corpse.\n"
              "It is wearing a fine silver necklace, and has several jeweled rings!\n\n")
        self.treasure += 4
        print(f"You have found {self.treasure} treasures so far.\n\n")

        if not self.flaming_sword:
            print("You pick up one of the troglodytes wooden clubs and light it in the small campfire,"
                  "creating a new torch.\n\n")
            print("You have acquired a torch!\n\n")
            self.torch_on = True

        print("You also notice a conspicuous looking boulder against the back wall.\n"
              "You push it away with some effort, revealing a small tunnel!\n"
              "following down the tunnel, the path leads to a stone corridor.\n\n")
        self.question3_torch_1()

    def question1(self):
        question_text = ("You come before a set of twin monolithic stone pillars.\n"
                         "Between these pillars, a ten foot wide, twenty-foot-high stone archway yawns open before "
                         "you.\n"
                         "It is dark, and potentially perilous to enter. Before you enter, would you like to:\n\n"
                         "A: Take a torch out of your pack and light it.\n"
                         "B: Strap on a pair of magical dark-vision goggles.\n"
                         "C: Plunge inside, heedless of the darkness.\n")
        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response == "A":
            self.torch_on = True
            print("Your torch blazes to life, illuminating the path before you!\n"
                  "You step into the maw of the dungeon corridor. It is dank, wet, and slimy in places,\n"
                  "and you take care to avoid slipping on the wet cobblestone that begins to sharply descend\n"
                  "as you delve deeper...")
            self.question2()

        elif response == "B":
            self.goggles_on = True
            print("You strap on a pair of gnomish night-vision goggles and plunge into the darkness.\n"
                  "You step into the maw of the dungeon corridor. It is dank, wet, and slimy in places,\n"
                  "and you take care to avoid slipping on the wet cobblestone as you delve deeper...")
            self.question2()

        elif response == "C":
            print("You plunge into the darkness, heedless of the danger, like the brave adventurer you are!\n"
                  "You step into the maw of the dungeon corridor. Blind as you are in the darkness, you grope about\n"
                  "in the darkness, trying to find your way deeper, and suddenly, you slip on something wet!\n"
                  "You lose your footing and stumble head over heels down the corridor that begins to sharply "
                  "descend!\n"
                  "You land on your head in a strange way, feel a crack that numbs your body, and black out!\n"
                  "You died!\n")
            self.prompt_restart()

    def prompt_restart(self):
        restart_input = input("Would you like to play again? (Type 'again' to restart): ").strip().lower()
        if restart_input == 'again':
            self.restart_game()
        else:
            print("Thanks for playing! Goodbye!")
            exit()

    def check_HP(self):
        if self.HP <= 0:
            print("Your wounds are too great, and you succumb to your fate.\n You are dead!\n")
            self.prompt_restart()

    def question2(self):
        question_text = ("\nThe air cools and the humidity rises as you descend deeper still into the dungeon.\n"
                         "The stone corridor you are traversing splits into two paths before you.\n"
                         "One path leads left - but is blocked by a large wooden door. \n"
                         "The other path leads right - but the path ends suddenly into a deep chasm-like pit.\n\n"
                         "A: Check out the door.\n"
                         "B: Look into the chasm.\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You try to open the door, but it is barred from the other side.\n")
            if self.torch_on:
                self.question2_1_torch()
            else:
                self.question2_2()

        elif response.upper() == "B":
            self.question3()

    def dwarf_king_attack(self):
        if self.dwarf_time_limit <= 0 and self.dwarf_king_dead == False:
            print("The dwarven king awakens, brandishing his battleaxe and says,\n"
                  "'You have dallied in my kingdom long enough! You are obviously"
                  "here to steal my treasures!'\n\n")
            self.dwarf_king_battle()

    def dwarven_throne_room(self):
        question_text = ("Looking about the throne room, you see three doors and one hatch in the ceiling.\n"
                         "There is an ornate wooden door against the left wall with a dwarven rune enscribed on it.\n"
                         "There is a sturdy looking stone door against the right wall.\n"
                         "There is an ornate metal vault door behind the throne against the back wall.\n"
                         "A dangling rope ladder leads to a small hatch in the ceiling.\n\n"

                         "A: Check out the Wooden door to the left.'\n"
                         "B: Inspect the Stone door to the right.'\n"
                         "C: Investigate the metal vault behind the throne.\n"
                         "D: Head toward the rope ladder.\n")

        valid_responses = {"A", "B", "C", "D"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("Upon closer inspection, the wooden door is enscribed with the dwarven runes 'WC'\n"
                  "The door is unlocked, so you take a look inside.\n")
            self.water_closet()

        if response.upper() == "B":
            if not self.stone_unlocked:
                if self.found_WC_key:
                    self.stone_unlocked = True
                    print("The stone door has a large pull handle, but as you test it, it seems locked.\n"
                          "you insert the stone key into the lock, and it clicks open!")
                    self.stone_room()
                else:
                    print("The stone door has a large pull handle, but as you test it, it seems locked.\n")
                    self.dwarf_time_limit = -1
                    self.dwarf_king_attack()
                    self.dwarven_throne_room()
            else:
                self.stone_room()

        if response.upper() == "C":
            self.vault_room()

        if response.upper() == "D":
            self.escape_hatch()

    def escape_hatch(self):
        question_text = ("You climb the rope ladder up to the hatch. Upon closer inspection, the hatch is labeled"
                         " 'Exit'.\n\n"

                         "A: Open the hatch and exit the lair!'\n"
                         "B: Return to the middle of the throne room.'\n")

        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            self.you_escaped()

        if response.upper() == "B":
            print("You climb back down, and make your way to the center of the room.\n")
            self.dwarven_throne_room()

    def stone_room(self):
        if not self.stone_pilfered:
            self.stone_pilfered = True
            print("Looking about the stone room, you find that it is a lavish bedroom."
                  "The opulent furniture is crafted\n"
                  "out of fine stone, and masterfully chiseled. Inside a footlocker at the base of the bed, you find\n"
                  "2 small sacks of gold!\n")
            print("Inside a dresser, you find 3 ornate jewel rings!\n"
                  "You pilfer the gold and rings, and then make your way back into the throne room.\n\n")

            self.treasure += 5
            print(f"You have acquired {self.treasure} treasures so far.\n\n")

            self.dwarf_time_limit = -1
            self.dwarf_king_attack()
            self.dwarven_throne_room()
        else:
            print("You look around the room again, but find nothing else of value. You return to the throne room.\n\n")
            self.dwarf_time_limit = -1
            self.dwarf_king_attack()
            self.dwarven_throne_room()

    def water_closet(self):
        question_text = ("Looking about, you can see that this room is a simple bathroom.\n"
                         "You look around and see a squat, but fully functional toilet, a porcelain tub, and a small"
                         "cabinet with a mirror \n\n"

                         "A: Use the toilet.'\n"
                         "B: Check inside the cabinet.'\n"
                         "C: Go back to the Throne Room.\n")
        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            if not self.check_peed:
                self.HP += 1
                print("You use the toilet. You feel a bit better!\n"
                      "You heal 1 HP.\n"
                      f"Current HP: {self.HP}\n")
                self.check_peed = True
            else:
                print("You try to go, but you don't need to use the toilet right now.\n")

            self.dwarf_time_limit = -1
            self.dwarf_king_attack()
            self.water_closet()

        if response.upper() == "B":
            if not self.found_WC_key:
                self.found_WC_key = True
                print("You check inside the cabinet, and find a diamond the size of an apple!\n"
                      "You also find a stone key!")
                self.treasure += 1
                self.key += 1
                print(f"You have acquired {self.treasure} treasures so far.\n\n")
            else:
                print("You look into the cabinet again, but find nothing else of value.\n")

            self.dwarf_time_limit = -1
            self.dwarf_king_attack()
            self.water_closet()

        if response.upper() == "C":
            print("You go back to the throne room.\n\n")
            self.dwarven_throne_room()

    def vault_room(self):
        if self.vault_locked:
            correct_order = ["A", "D", "C"]
            current_input_index = 0
            valid_responses = ["A", "B", "C", "D", "E"]

            print("You walk up to the ornate metal vault door behind the throne.\n"
                  "The locked vault door has a large free-turning wheel in the center,\n"
                  "presumably used to unlock the safe with a series of clockwise and counter-clockwise turns.\n\n")

            while current_input_index < len(correct_order):
                user_input = self.get_valid_input("A: Turn the wheel clockwise 90 degrees.\n"
                                                  "B: Turn the wheel clockwise 180 degrees.\n"
                                                  "C: Turn the wheel counter-clockwise 90 degrees.\n"
                                                  "D: Turn the wheel counter-clockwise 180 degrees.\n"
                                                  "E: Return to the throne room.\n\n", valid_responses)

                if user_input == "E":
                    print("The safe remains locked, and you retreat.")
                    self.dwarven_throne_room()

                elif user_input == "B":
                    print("There is a deep thunk, and the wheel locks for a moment. You just reset the wheel.")
                    current_input_index = 0

                elif user_input in correct_order:
                    if user_input == correct_order[current_input_index]:
                        print("Mechanisms in the vault groan and thunk into place! You're on the right track!")
                        current_input_index += 1
                    else:
                        print("There is a deep thunk, and the wheel locks for a moment. You just reset the wheel.")
                        current_input_index = 0

            self.treasure += 12
            print("There is a cacophony of whirring gears and the slam of pins dropping into place!\n"
                  "The safe is now unlocked! Looking inside, you find an enormous bag of precious gems!\n"
                  "You walk back into the throne room.\n\n"
                  f"You have found {self.treasure} treasures so far.\n\n")
            self.vault_locked = False
            self.dwarven_throne_room()
        else:
            print("You walk up to the opened vault. There is nothing else of value inside."
                  "You turn back to the throne room.")
            self.dwarven_throne_room()

    def dwarf_king_battle(self):

        verbs = ["clobber", "smack", "pound", "beat"]
        print("You and the Dwarf King begin an epic battle!")

        while self.HP > 0 and self.dwarf_king_HP > 0:
            # Player attacks Dwarf King
            if self.flaming_sword:
                if random.random() <= 0.8:
                    attack_verb = random.choice(verbs)
                    self.dwarf_king_HP -= 1
                    print(f"You {attack_verb} the Dwarf King with your flaming Sword!"
                          f" Dwarf King's HP:", self.dwarf_king_HP)
                else:
                    print("You miss the Dwarf King!")

            if not self.flaming_sword:
                if random.random() < 0.5:
                    attack_verb = random.choice(verbs)
                    self.dwarf_king_HP -= 1
                    print(f"You {attack_verb} the Dwarf King with your torch! Dwarf King's HP:", self.dwarf_king_HP)
                else:
                    print("You miss the Dwarf King!")

            # Check if Dwarf King is defeated
            if self.dwarf_king_HP <= 0:
                print("Congratulations! You defeated the Dwarf King! You take his stone crown as a trophy.\n\n")
                self.treasure += 1
                print(f"You have {self.treasure} treasures so far.\n\n")
                self.dwarf_king_dead = True
                break

            # Dwarf King attacks the player
            if random.random() < 0.5:
                attack_verb = random.choice(verbs)
                self.HP -= 1
                print(f"The Dwarf King {attack_verb}s you with his battleaxe! Your HP:", self.HP)
            else:
                print("The Dwarf King misses you!")

            # Check if player is defeated
            if self.HP <= 0:
                print("You were defeated by the Dwarf King. Game Over!")
                self.prompt_restart()
                break

        print("The battle has ended, and you are victorious! Now you can look about this place unimpeded.\n")
        self.dwarven_throne_room()

    def question5_torch_final(self):
        question_text = ("You enter into an ornate throne room. In the center, seated upon a large stone chair\n"
                         "you see a dwarf with a truly magnificent beard. The dwarf is wearing a jagged stone\n"
                         "crown upon its head, and resting in its grip, you see a huge stone battleaxe.\n"
                         "'I am the Stone Craftsdwarf King!\n"
                         "I demand to know why you are scuttling about my stony domain!'\n\n"

                         "A: Say, 'I'm here to plunder your treasure, Craftsdwarf King!'\n"
                         "B: Say, 'Sorry, I was looking for a bathroom and got lost.'\n"
                         "C: Charge the dwarven king - swinging your torch with reckless abandon\n")

        valid_responses = {"A", "B", "C", "D"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("'Oh no you don't!' The dwarven king charges you faster than you'd think a dwarf could move!\n")
            self.dwarf_king_battle()

        elif response.upper() == "B":
            print("'Oh. Well then. My royal bathroom is over yonder. Use it, and see yourself out of my home.'\n"
                  "The dwarven king shoos you off with a hand-wave, and promptly falls asleep. I guess as long\n"
                  "as you're quiet, you might be able to plunder the king's treasure without him noticing!\n")
            self.dwarven_throne_room()

        elif response.upper() == "C":
            print("'You rapscallion!' The dwarven king is caught by surprise as you preemptively attack him!\n"
                  "The dwarven king takes one wound. He jumps up, battleaxe at the ready!\n")
            self.dwarf_king_HP -= 1
            self.dwarf_king_battle()

    def time_limit_dogs(self):
        question_text = ("\nA pack of horrifying mutated dogs with multiple legs, eyes, ears, and mouths corner you!\n"
                         "A: Try to run away.\n"
                         "B: Stay and fight them off.\n")

        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            if self.flaming_sword:
                print("You barely manage to fend them off with your flaming sword as you retreat.\n"
                      "The dogs retreat for now...\n")
                self.question4_torch_reset()

            else:
                print("You try to run away from them, but they are too fast and they run you down!\n"
                      "They tear you apart!\n"
                      "You have died!\n\n")
                self.prompt_restart()

        elif response.upper() == "B":
            if self.flaming_sword:
                print("You stand and fight the mutated dogs with your flaming sword!\n"
                      "You cut them down, one after another as they charge, and you slay them all!\n"
                      "These dogs shouldn't trouble you any longer.\n")
                self.dogs_dead = True

                self.question4_torch_reset()
            else:
                print("You stand and fight them off with your torch, but one scored a savage bite. -1 HP.\n"
                      "The dogs retreat for now...\n")
                self.HP -= 1
                print(f"Current HP: {self.HP}\n")
                self.check_HP()
                self.question4_torch_reset()

    def question4_torch_reset(self):
        question_text = ("You are still in a very large room filled with thick pillars.\n"
                         "The ceiling is low, but as you look down each row of pillars, there is seemingly"
                         "no end in sight.\n"

                         "A: Continue to walk along the left edge of the room to try and find another door or exit.\n"
                         "B: Continue to walk along the right edge of the room to try and find another door or exit.\n"
                         "C: Plunge forward, deeper into the strange room of pillars.\n")

        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You continue to walk along the left edge of the room for what seems like thirty more minutes,\n"
                  "with no end in sight.\n")

            if self.dogs_dead:
                print("There doesn't seem to be anything else in this direction...\n")
                self.question4_torch_reset()

            else:
                print("The silence of your long walk is broken by another series of guttural growls\n"
                      "and high pitched yips that echo out around you. The mutated dogs are hounding you again!\n")
                self.time_limit_dogs()

        if response.upper() == "B":
            print("You continue to walk along the right edge of the room for what seems like thirty more minutes,\n"
                  "with no end in sight.\n")

            if self.dogs_dead:
                print("There doesn't seem to be anything else in this direction...\n")
                self.question4_torch_reset()

            else:
                print("The silence of your long walk is broken by another series of guttural growls\n"
                      "and high pitched yips that echo out around you. The mutated dogs are hounding you again!\n")
            self.time_limit_dogs()

        elif response.upper() == "C":
            print("You plunge deeper into the room filled with strange pillars\n")
            self.question4_torch_pillar_1()

    def question4_torch_pillar_1(self):
        question_text = ("\nYou are within the large sea of pillars in this room, searching for an exit,\n"
                         "or for treasure to be had\n\n"
                         "A: Aimlessly meander towards the left.\n"
                         "B: Aimlessly meander towards the right.\n"
                         "C: Keep following a line of pillars directly straight.\n")
        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            if not self.found_pillar_key:
                self.found_pillar_key = True
                self.key += 1
                print("You walk left, through the forest of pillars. Amongst some rubble and bracken on the dungeon\n"
                      "floor, you discover a rather over-sized brass key!\n\n"
                      "Found: 1 Brass Key")
            else:
                print("You continue to meander left, but find nothing of note or value...\n")
                if not self.dogs_dead:
                    self.dog_time_limit = -1
                    if self.dog_time_limit <= 0:
                        self.time_limit_dogs()
            self.question4_torch_pillar_1()

        if response.upper() == "B":
            if not self.found_pillar_potion:
                self.found_pillar_potion = True
                self.HP += 1
                print("You walk left, through the vast expanse of stone pillars. You find a small discarded satchel\n"
                      "containing a HealMeUp brand potion of health! You drink it, and gain +1 HP\n")
                print(f"Current HP: {self.HP}")
            else:
                print("You continue to meander right, but find nothing of note or value...\n")
                if not self.dogs_dead:
                    self.dog_time_limit = -1
                    if self.dog_time_limit <= 0:
                        self.time_limit_dogs()
            self.question4_torch_pillar_1()

        if response.upper() == "C":
            print("You continue straight. Eventually, you come to the other side of this massive room.\n"
                  "You find a large iron door with no handle. The door has a single keyhole in its center \n")
            if self.key >= 1:
                print("You fit a key into the door and it unlocks!\n\n")
                self.question5_torch_final()
            else:
                print("You have no key to place in this door. Perhaps there is a key somewhere in this room?\n"
                      "You turn back, and begin looking around the room again.\n\n")
                if not self.dogs_dead:
                    self.dog_time_limit = -1
                    if self.dog_time_limit <= 0:
                        self.time_limit_dogs()
                self.question4_torch_pillar_1()

    def question3_torch_1(self):
        question_text = ("You walk down the corridor into a room filled with thick pillars.\n"
                         "The ceiling is low, but as you look down each row of pillars, you see there is seemingly\n"
                         "no end in sight.\n\n"
                         "A: Walk along the left edge of the room to try and find another door or exit.\n"
                         "B: Walk along the right edge of the room to try and find another door or exit.\n"
                         "C: Plunge forward, deeper into the strange room of pillars.\n")

        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You walk along the left edge of the room for what seems like thirty minutes, with no end in\n"
                  "sight. The silence of your long walk is broken by a series of guttural growls and high pitched\n"
                  "yips that echo out around you.\n")
            self.time_limit_dogs()

        elif response.upper() == "B":
            print("You walk along the right edge of the room for what seems like thirty minutes, with no end in\n"
                  "sight. The silence of your long walk is broken by a series of guttural growls and high pitched\n"
                  "yips that echo out around you.\n")
            self.time_limit_dogs()

        elif response.upper() == "C":
            print("You walk forward, into the strange room filled with a seemingly endless number of pillars.\n")
            self.question4_torch_pillar_1()

    def question2_1_torch(self):
        question_text = ("A: Try to break the door down.\n"
                         "B: Set the door alight with your torch to weaken it first.\n"
                         "C: Check out the chasm.\n\n")
        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You attempt to shoulder through the thick wooden door, but it is made of sturdy wood and\n"
                  "banded together with thick iron. You only end up hurting yourself, and take 1 wound.\n"
                  "You do not forsee brute force being an option.\n")
            self.HP -= 1
            print(f"Current HP: {self.HP}")
            self.check_HP()
            self.question2_1_torch()

        elif response.upper() == "B":
            print("You set the door alight! It slowly burns and weakens enough for you to break it down!\n")
            self.question3_torch_1()

        elif response.upper() == "C":
            self.question3()

    def question2_2(self):
        question_text = ("A: Try to break the door down.\n"
                         "B: Look into the chasm.\n")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You attempt to shoulder through the thick wooden door, but it is made of sturdy wood and\n"
                  "banded together with thick iron. You only end up hurting yourself, and take 1 wound.\n"
                  "You do not forsee brute force being an option.\n")
            self.HP -= 1
            print(f"Current HP: {self.HP}")
            self.check_HP()
            self.question2_2()

        elif response.upper() == "B":
            self.question3()


if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
