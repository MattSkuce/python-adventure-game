import random


class AdventureGame:
    def __init__(self):
        self.goggles_on = False
        self.torch_on = False
        self.HP = 3
        self.dwarf_king_HP = 2
        self.key = 0
        self.treasure = 0
        self.dog_time_limit = 3
        self.dwarf_time_limit = 2
        self.dwarf_king_dead = False
        self.found_pillar_key = False
        self.found_pillar_potion = False
        self.found_WC_key = False
        self.stone_unlocked = False
        self.stone_pilfered = False
        self.vault_locked = True

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
        self.HP = 3
        self.dwarf_king_HP = 2
        self.key = 0
        self.treasure = 0
        self.dog_time_limit = 3
        self.dwarf_time_limit = 2
        self.dwarf_king_dead = False
        self.found_pillar_key = False
        self.found_pillar_potion = False
        self.found_WC_key = False
        self.stone_unlocked = False
        self.stone_pilfered = False

    def start_game(self):
        print("Welcome to the Dark Dungeon \nYour mission is to find the treasure.")
        self.question1()

    def question3(self):  # TODO
        question_text = (f"You look over the edge of the chasm. With {'goggles on' if self.goggles_on else
        'torch burning brightly'}, you see a pool of water, thirty feet below...")
        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response == "A":
            print("Chasm question 3: Response: A")  # TODO
        elif response == "B":
            print("Chasm question 3: Response: B")  # TODO

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
        restart_input = input("Would you like to retry? (Type 'retry' to restart): ").strip().lower()
        if restart_input == 'retry':
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
        question_text = ("Looking about the throne room, you see three doors.\n"
                         "There is an ornate wooden door against the left wall with a dwarven rune enscribed on it.\n"
                         "There is a sturdy looking stone door against the right wall.\n"
                         "There is an ornate metal vault door behind the throne against the back wall.\n"

                         "A: Check out the Wooden door to the left.'\n"
                         "B: Inspect the Stone door to the right.'\n"
                         "C: Investigate the metal vault behind the throne.\n")

        valid_responses = {"A", "B", "C"}
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
            self.HP += 1
            print("You use the toilet. You feel a bit better!\n"
                  "You heal 1 HP.\n"
                  f"Current HP: {self.HP}\n")
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

        verbs = ["clobbered", "smacked", "wailed on", "beat"]
        print("You and the Dwarf King begin an epic battle!")

        while self.HP > 0 and self.dwarf_king_HP > 0:
            # Player attacks Dwarf King
            if random.random() < 0.5:
                attack_verb = random.choice(verbs)
                self.dwarf_king_HP -= 1
                print(f"You {attack_verb} the Dwarf King with your torch! Dwarf King's HP:", self.dwarf_king_HP)
            else:
                print("You miss the Dwarf King!")

            # Check if Dwarf King is defeated
            if self.dwarf_king_HP <= 0:
                print("Congratulations! You defeated the Dwarf King!")
                self.dwarf_king_dead = True
                break

            # Dwarf King attacks the player
            if random.random() < 0.5:
                attack_verb = random.choice(verbs)
                self.HP -= 1
                print(f"The Dwarf King {attack_verb} you with his battleaxe! Your HP:", self.HP)
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
            print("'You rapscallion!' The dwarven king is caught by surprise as you bean him on the head"
                  "with your torch!\n"
                  "The dwarven king takes one wound. He jumps up, battleaxe at the ready!\n")
            self.dwarf_king_HP -= 1
            self.dwarf_king_battle()

    def question4_torch_1(self):
        question_text = ("\nA pack of horrifying mutated dogs with multiple legs, eyes, ears, and mouths corner you!\n"
                         "A: Try to run away.\n"
                         "B: Stay and fight them off.\n")

        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You try to run away from them, but they are too fast and they run you down!\n You die!\n")
            self.prompt_restart()

        elif response.upper() == "B":
            print("You stand and fight them off with your torch, but one scored a savage bite, and you take a wound.\n"
                  "The dogs retreat for now...\n")
            self.HP -= 1
            print(f"Current HP: {self.HP}\n")
            self.check_HP()
            self.question4_torch_reset()

    def time_limit_dogs(self):
        question_text = ("\nA pack of horrifying mutated dogs with multiple legs, eyes, ears, and mouths corner you!\n"
                         "A: Try to run away.\n"
                         "B: Stay and fight them off.\n")

        valid_responses = {"A", "B"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You try to run away from them, but they are too fast and they run you down!\n You die!\n")
            self.prompt_restart()

        elif response.upper() == "B":
            print("You stand and fight them off with your torch, but one scored a savage bite, and you take a wound.\n"
                  "The dogs retreat for now...\n")
            self.HP -= 1
            print(f"Current HP: {self.HP}\n")
            self.check_HP()
            self.question4_torch_pillar_1()

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
                  "with no end in sight. The silence of your long walk is broken by another series of guttural growls\n"
                  "and high pitched yips that echo out around you. The mutated dogs are hounding you again!\n")
            self.question4_torch_1()

        elif response.upper() == "B":
            print("You continue to walk along the right edge of the room for what seems like thirty more minutes,\n"
                  "with no end in sight. The silence of your long walk is broken by another series of guttural growls\n"
                  "and high pitched yips that echo out around you. The mutated dogs are hounding you again!\n")
            self.question4_torch_1()

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
                self.dog_time_limit -= 1
                if self.dog_time_limit <= 0:
                    self.time_limit_dogs()
                self.question4_torch_pillar_1()

    def question3_torch_1(self):
        question_text = ("Pushing your way past the burnt remnants of the door, you walk down a corridor that splits\n"
                         "into a room filled with thick pillars. The ceiling is low, but as you look down each row of\n"
                         "pillars, you see there is seemingly no end in sight.\n"
                         "A: Walk along the left edge of the room to try and find another door or exit.\n"
                         "B: Walk along the right edge of the room to try and find another door or exit.\n"
                         "C: Plunge forward, deeper into the strange room of pillars.\n")

        valid_responses = {"A", "B", "C"}
        response = self.get_valid_input(question_text, valid_responses)

        if response.upper() == "A":
            print("You walk along the left edge of the room for what seems like thirty minutes, with no end in\n"
                  "sight. The silence of your long walk is broken by a series of guttural growls and high pitched\n"
                  "yips that echo out around you.\n")
            self.question4_torch_1()

        elif response.upper() == "B":
            print("You walk along the right edge of the room for what seems like thirty minutes, with no end in\n"
                  "sight. The silence of your long walk is broken by a series of guttural growls and high pitched\n"
                  "yips that echo out around you.\n")
            self.question4_torch_1()

        elif response.upper() == "C":
            print("You walk forward, into the strange room filled with a seemingly endless number of pillars.\n")
            self.question4_torch_pillar_1()

    def question2_1_torch(self):
        question_text = ("A: Try to break the door down.\n"
                         "B: Set the door alight with your torch to weaken it first.\n")
        valid_responses = {"A", "B"}
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
