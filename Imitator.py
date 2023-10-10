"""Imitator, a 3+ player game
A player click the starts button and passes the calc to the said person(specified by game)
The reciving player clicks the EXE button and the game will choose if he 
is the one that should imitate that he knows what are they talking about,
or if he knows what to talk about. this is repeated to all players.
The players ask questions to each others. the game will tell who to question whom.
Finally when the game finishes the players vote to who they think is imitating.
after voting the imitator will try to guess the subject they were talking about

useful info:
-when adding player type 1qa as a player name to add to add 3 dummy players
-batch add names by adding comma between every name(example: Noah,Hamed,Ali)
while in questions menu type 1 then enter to quit game
"""

"""Change log:
1.1:
added confirmaion dialog when passing device to player
added new ideas to play with
fixed some stuff going off screen

1.2:
fixed a bug in adding players
fixed errors when typing something not expected like typing a string when the program is expecting a number

1.3
fixed a bug when removing players
removed roles list as it is useless
imitator assist an option that makes the game  bit easier for the imitator
the random choosing will now have less duplicates
quit game feature

1.4
fixed crash when typing text instead of a number
improved menus
    |_players
    |_credits
    |_settings
    |_role
    |_questions
removed unused menus
    |_vote (unused)
    |_remove player (replaced)

1.4.1
fixed text cutoff
minor player menu changes

"""


from random import randint
from random import choice as choose
from String_methodes import *

NAME = "Imitator"
VERSION = "1.4.1"
CREATION_DATE = "30/May/2023"


ANIMALS = {
    "Dog": "A loyal animal, often a pet.",
    "Cat": "An independent animal, often a pet.",
    "Horse": "A large and powerful animal used for transportation.",
    "Cow": "A large and docile animal, used for milk and meat.",
    "Chicken": "A small and social animal, used for eggs and meat.",
    "Fish": "A cold-blooded vertebrate that lives in water.",
    "Bird": "A warm-blooded vertebrate that has feathers and wings.",
    "Elephant": "The largest land animal on Earth.",
    "Giraffe": "The tallest land animal on Earth.",
    "Lion": "A large, powerful animal, the king of the jungle.",
    "Tiger": "A large, striped animal. it's the same as Lion",
    "Bear": "A large, furry mammal that can be found in North America, Europe, and Asia.",
    "Monkey": "A small, furry mammal that has a long tail and lives in trees.",
    "Dolphin": "A marine mammal, related to whales and porpoises.",
    "Shark": "A large, predatory fish that has sharp teeth.",
    "Octopus": "A marine creature with eight arms and a beak.",
    "Snail": "A creature with a soft body and a shell. it is slow",
    "Bee": "An insect that makes honey.",
    "Ant": "An insect that lives in colonies and works together to gather food.",
    "Grasshopper": "An insect that jumps and eats plants.",
    "Cockroach": "An insect, often considered a pest.",
    "Spider": "An arthropod with eight legs.",
    "Scorpion": "An arthropod with a long, thin body and a stinger.",
    "Snake": "A long, legless reptile that has scales.",
    "Lizard": "A reptile with a long tail and scales.",
    "Turtle": "A reptile with a hard shell that protects its body.",
    "Chameleon": "A lizard that can change its color to blend in with its surroundings.",
    "Jellyfish": "A marine creature with a bell-shaped body and tentacles.",
    "Whale": "A large, marine mammal, the largest animal on Earth.",
}

FOODS = {
    "Pizza": "flatbread topped with tomato sauce and other toppings.",
    "Pasta": "type of noodle, often served with sauces.",
    "Burger": "sandwich but rounded, with meat",
    "Fried chicken": "Chicken, coated in a batter or breading and then fried.",
    "Steak": "A cut of beef, grilled or pan-fried.",
    "French fries": "deep-fried potato fingers.",
    "Broast" : "dish made of fried chicken and fried potato.",
    "Salad": "dish of cut vegetables.",
    "Soup": "liquid dish, often made with vegetables",
    "Sandwich": "Two pieces of bread with toppings.",
    "Tacos": "Mexican dish made with a corn tortilla",
    "Burritos": "Mexican dish made with a flour tortilla",
    "Sushi": "Japanese dish made with ricem and fish.",
}

OBJECTS = {
    'chair': 'A piece of furniture with four legs and a seat.',
    'table': 'A piece of furniture with a flat top and legs.',
    'computer': 'A device that is used to process information.',
    'phone': 'A device that is used to make and receive calls.',
    'book': 'A collection of written or printed pages.',
    'pen': 'A writing instrument with a pointed tip.',
    'pencil': 'A writing instrument with a flat tip.',
    'eraser': 'A tool used to remove marks from paper.',
    'ruler': 'A tool used to measure distances.',
    'marker': 'A tool used to write on a board.',
    'hat': 'A covering for the head.',
    'shirt': 'A piece of clothing worn on the upper body.',
    'pants': 'A covering for the lower body.',
    'umbrella': 'A covering used to protect from rain or sun.',
    'watch': 'A device that tells time.',
    'phone case': 'A case for a phone.',
    'ball': 'A toy that is round and bounces.',
    'glove': 'A piece of clothing worn on the hands.'
}





def check_name(name, check_comma = True):
    if len(name) > 9 or len(name) <= 0:
        warn("Player name too long/ too short. max. 9 letters and min.1 letter")
        return False

    try: players.index(name)
    except ValueError:pass # name not duplicate
    else:
        warn("name is duplicate")
        return False

    if check_comma:
        for i in list(name):
            if i not in PLAYER_NAME_ALLOWED_LETTERS:
                warn("Player not added. Name contained unallowed letters.")
                return False
    else:
        PLAYER_NAME_ALLOWED_LETTERS.append(",")
        for i in list(name):
            if i not in PLAYER_NAME_ALLOWED_LETTERS:
                warn("Player not added. Name contained unallowed letters.")
                PLAYER_NAME_ALLOWED_LETTERS.remove(",")
                return False
        PLAYER_NAME_ALLOWED_LETTERS.remove(",")
    
    





no_of_questions = 5
imitator_assist = True 
"""imitator assist setting
desc: makes the game easier for imitator
gameplay effects:
-if there are more than 3 players the imitator will never be asked
-when a player is an imitator the game will tell the type of the idea (example: object, food, animal)"""
players = []
PLAYER_NAME_ALLOWED_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

MAIN_MENU = """{0}!
1.Play
2.Players
3.Settings
----0:Quit----
""".format(NAME)
PLAYERS_MENU = """Manage players
1.Add 
2.Back 
3.Remove
4.View players
"""
SETTINGS_MENU = """Settings
1.No. questions: {0}
2.Credits
3.Imitator assist:
{1}
----(0:cancel)----
"""
ADD_PLAYER_MENU = """Type the name of
the player to add.

Seperate names by ','
to batch add names
-(1:cancel)-
"""
ROLE_MENU = """{0}
You are an:
{1}.
{2}
Dont tell anyone!"""
QUESTION_MENU = """Questions({0}/{1})
Hey {2},
ask {3}.
Done? press exe"""
CREDITS_MENU="""Credits
{game_name} {version}
by blabla_lab (H.A)
Good luck,
{role}
""".format(game_name = NAME, version=VERSION, role=choose(["Imitator", "Innocent"]))


invalid = False
while True:
    vote=[]
    clr_scrn()
    
    try:user_input = int(input(MAIN_MENU))
    except (TypeError, ValueError): continue


    if user_input == 0:
        clr_scrn()
        raise SystemExit("Quit")
    if user_input == 3:
        # settings
        clr_scrn()
        
        
        try:user_input = int(input(SETTINGS_MENU.format(no_of_questions, imitator_assist)))
        except (TypeError, ValueError): continue
        
        if user_input == 1:
            clr_scrn()
            try:user_input = int(input(add_line_breaks("No. of questions to be asked:")))
            except ValueError: continue
            if user_input < 0 or user_input > 50: continue
            no_of_questions = user_input
        elif user_input == 2:
            clr_scrn()
            warn(CREDITS_MENU, False)
        elif user_input == 3:
            s = ask("Turn on imitator assist to make the game easier?", ["yes","no", "learn more"], prompt=False)
            if s == "yes":
                imitator_assist = True
            elif s == "no":
                imitator_assist = False
            elif s == "learn more":
                warn("Easier for imitator: tell type of idea, not first answerer when more than 3 players.")

    elif user_input == 2:
        # add player
        while True:
            clr_scrn()

            try:user_input = int(input(PLAYERS_MENU))
            except (TypeError, ValueError): continue
            
            if user_input == 2 or user_input is None:
                break
            elif user_input == 4:
                clr_scrn()
                view_list(players, title="--Players--", readonly=True)
            elif user_input == 3:
                clr_scrn()
                user_input = view_list(players, title="--Remove Player--")
                try:players.remove(user_input)
                except IndexError: warn("Player not found")
                else:warn("Removed player:\n{}".format(user_input))


            elif user_input == 1:
                clr_scrn()
                new_player_name = input(ADD_PLAYER_MENU).strip().replace("  ", " ")
                if new_player_name == "1" or user_input is None:
                    warn("Player name not\nadded.\nPress EXE", False)
                    continue
                if new_player_name == "1qa":
                    # players.extend(iter(["DumOne","DumTwo", "DumThree"]))
                    new_player_name = "DumOne,DumTwo,DumThree"

                if new_player_name.find(","):
                    for i in new_player_name.split(","):
                        if check_name(i, False) is False:
                            warn("operation stopped")
                            break
                        else:
                            players.append(i)
                            warn("Added player:\n{}".format(i))
                    continue
                else:
                    if check_name(new_player_name) is False:
                        continue

                players.append(new_player_name)
                warn("Added player:\n{}".format(new_player_name))
                new_player_name = None
    elif user_input == 1:
        quit_game = False
        # play
        if len(players) <= 2:
            warn("The game needs at least 3 players to start.")
            continue

        # the game
        catagory = randint(1,3)
        if catagory == 1:
            idea = choose((list(ANIMALS.keys())))
            definition = ANIMALS[idea]
        elif catagory == 2:
            idea = choose((list(FOODS.keys())))
            definition = FOODS[idea]
        elif catagory == 3:
            idea = choose((list(OBJECTS.keys())))
            definition = OBJECTS[idea]





        Imitator = choose(players)
        idea_hint = "Sorry, but I \ncan't help you"
        if imitator_assist:
            if catagory == 1:
                idea_hint = "a animal"
            elif catagory == 2:
                idea_hint = "a food"
            elif catagory == 3:
                idea_hint = "a object"


        for i in range(0,len(players)):
            warn("PASS THE DEVICE TO\n{}".format(players[i]), auto_break_lines=False)
            while True:
                if not ask("Are you {}?".format(players[i]), ["Im {}".format(players[i]), "Im not {}".format(players[i])], prompt=False) == "Im {}".format(players[i]):continue
                else: break
                
            warn(ROLE_MENU.format(
                    players[i],
                    "Imitator" if Imitator == players[i] else "Innocent",
                    "idea is {idea}:".format(idea = idea)
                    if Imitator != players[i]
                    else "Try to guess idea",
                ),
                False,
            )
            if Imitator == players[i]:
                if imitator_assist:
                    warn("Goodluck, try to ask questions that help identify idea\nalso the idea is {hint}".format(hint = idea_hint))
                else:
                    warn("Goodluck, try to ask questions that help identify idea")
            else:
                warn("definition of {0}:{1}".format(idea, definition),auto_break_lines_every = 20)

        warn("Pass the device to someone to announce who to ask whom.")
        prev_asker_player = ""
        for i in range(0, no_of_questions):
            while True:
                asker = choose(players)
                answerer = choose(players)
                if asker == answerer:
                    continue
                if imitator_assist:
                    if i == 0 and len(players) >= 4:
                        if answerer == Imitator:
                            continue
                if asker == prev_asker_player:
                    continue
                else:
                    prev_asker_player = asker
                    break
            if warn(QUESTION_MENU.format(i, no_of_questions, asker, answerer), False) == "1":
                if ask("You pressed 1\n\nQuit game?", prompt=False) == "yes":
                    quit_game = True
                    break
                else:continue
                
            
        for i in range(0,len(players)):
            if quit_game:break
            warn("PASS THE DEVICE TO\n{}".format(players[i]), auto_break_lines=False)
            vote.append(view_list(players, title="--Who's Imitator?--"))

        try:
            warn("Time to reveal the\nimitator...\npress EXE to reveal", False)
            warn("The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}".format(max(set(vote), key=vote.count),Imitator), False)
        except ValueError: warn("The game was quit by the admin")
        warn("Game finished")
        
