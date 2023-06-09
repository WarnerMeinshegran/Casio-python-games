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
"""


from random import randint
from random import choice as choose

NAME = "Imitator"
VERSION = 1.3
CREATION_DATE = "30/May/2023"
LAST_UPDATE_DATE = "1/June/2023"

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


def clr_scrn():
    '''clears screen by making new lines'''    
    print("\n"*7)


def _int(x): 
    try: int(x) 
    except (ValueError, TypeError): return None
    else: return int(x)

def _str(x): 
    try: str(x) 
    except (ValueError, TypeError): return None
    else: return str(x)



def int_input(message):
    while True:
        z = input(message)
        if z is None or z.strip() == "":
            print("Please enter a number")
            clr_scrn()
            continue
        return _int(z)


def str_input(message):
    while True:
        z = input(message)
        if z is None or z.strip() == "":
            print("Please enter text")
            clr_scrn()
            continue
        return _str(z)


def add_line_breaks(string, every=20):
    """
    This function takes a string and puts "/n" every 20 letters.

    Args:
      string: The string to add line breaks to.
      every: break line every number of letters

    Returns:
      A new string with line breaks added every 20 letters.
    """
    string = string.strip()

    new_string = ""
    for i in range(len(string)):
        if i % every == 0: # if index is divisable by 20
            new_string += "\n" if string[i] in [" ", ".", ","] else "-\n"
        new_string += string[i]
    result = "\n".join(new_string.strip().split("\n")).strip()
    result2 = [i.strip() for i in result.split("\n")]
    return "\n".join(result2)


def warn(message, auto_break_lines = True, auto_break_lines_every= 20):
    '''Prints the given message ans waits for the user to press enter

    Args:
        message (str): the message to display
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.
    '''    
    clr_scrn()
    if auto_break_lines: s = input(add_line_breaks(message, auto_break_lines_every))
    else:s = input(message)
    clr_scrn()
    return s

def ask(question, ans = None, auto_break_lines = True, auto_break_lines_every = 20, prompt = True):
    '''just like warn but instead asks the user for an input of number like choosing an option

    Args:
        question (str): the question to ask
        ans (list, optional): an list of all answers (recommended max: 3-4 answers). Defaults to ["yes","no"].
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.

    Returns:
        str: the answer choosen not the index
    '''    
    if ans is None:
        ans = ["yes","no"]
    while True:
        
        if prompt:warn("{question}\n\npress exe".format(question=question), auto_break_lines, auto_break_lines_every)
        else:print(add_line_breaks(question))

        print("-", end="")
        try: user_input = int(input("{}\n".format("\n-".join(ans))))
        except (ValueError,TypeError): continue

        try: user_input -= 1
        except TypeError: continue

        if user_input < 0:
            continue
        clr_scrn()
        try: return ans[user_input]
        except IndexError: continue


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

MAIN_MENU = """{0}
1.Play
2.Players
3.Settings
----0:Quit----
""".format(NAME)
PLAYERS_MENU = """Plrs:{0}
-1.add 2.back 3.rmv
4.all plrs-
"""
SETTINGS_MENU = """Settings
1.No. questions: {0}
2.Credits
3.Imitator assist:
{1}
----(0:cancel)----
"""
ADD_PLAYER_MENU = """Whats the name
of the player you
want to add?
seperate names by ','
to batch add names
-(1:cancel)-
"""
REMOVE_PLAYER_MENU = """{}
Name of plr to rmv:
-(1:cancel)-
"""
ROLE_MENU = """{0}
You are an:
{1}.
{2}
dont tell anyone!
press exe to continue"""
QUESTION_MENU = """Questions({0}/{1})
Hey {2},
ask {3}.
when done press EXE"""
VOTE_MENU = """Hey {0},
who's imitating?
{1}"""
CREDITS_MENU="""Credits
{game_name} {version}
by blabla_lab (H.A)
Thanks for playing.
""".format(game_name = NAME, version=VERSION)


invalid = False
while True:
    vote=[]
    clr_scrn()
    user_input = int_input(MAIN_MENU)
    if user_input == 0:
        clr_scrn()
        raise SystemExit("Quit")
    if user_input == 3:
        # settings
        clr_scrn()
        user_input = int_input(SETTINGS_MENU.format(no_of_questions, imitator_assist))
        if user_input == 1:
            clr_scrn()
            try:user_input = int_input("No. of questions to be asked:")
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
            user_input = int_input(PLAYERS_MENU.format("\n".join(players)))
            if user_input == 2 or user_input is None:
                break
                
            elif user_input == 4:
                clr_scrn()
                warn("\n".join(players), False)
            elif user_input == 3:
                clr_scrn()
                user_input = ask("type the index of the player to remove", players)
                if user_input == "1":
                    warn("Player name not\nremoved.\nPress EXE", False)
                    continue
                players.remove(user_input)
                warn("removed player:\n{}".format(user_input))


            elif user_input == 1:
                clr_scrn()
                new_player_name = str_input(ADD_PLAYER_MENU).strip().replace("  ", " ")
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
            warn("not enough players")
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
        idea_hint = "Sorry, but I \ncant help you"
        if imitator_assist:
            if catagory == 1:
                idea_hint = "a animal"
            elif catagory == 2:
                idea_hint = "a food"
            elif catagory == 3:
                idea_hint = "a object"


        for i in range(0,len(players)):
            warn("PASS THE DEVICE TO {}".format(players[i]))
            while True:
                if not ask("PRESS 1 TO CONFIRM YOU ARE {}".format(players[i]), ["Im {}".format(players[i]), "Im not {}".format(players[i])], prompt=False) == "Im {}".format(players[i]):continue
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
            warn("PASS THE DEVICE TO {}".format(players[i]))
            vote.append(ask("Who is imitating to\nunderstand the speech\nsubject?", players, False))

        try:
            warn("Time to reveal the\nimitator...\npress EXE to reveal", False)
            warn("The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}".format(max(set(vote), key=vote.count),Imitator), False)
        except ValueError: warn("The game was quit by the admin")
        warn("Game finished")
        
