"""Imitator, a 3+ player game
How to:
A player click the starts button and passes the calc to the said person(specified by game)
The reciving player clicks the show button and the game will choose if he 
is the one that should imitate that he knows what are they talking about,
or if he knows what to talk about. this is repeated to all players.
The player ask questions to each others. the game will tell who to question whom.
Finally when the game finishes the players vote to who they think who is imitating.
after voting the imitator will try to guess the subject they were talking about

useful info:
-when adding player type 1qa as a player name to add to add 3 dummy players
-batch add / remove names by adding comma between every name(example: Noah,Hamed,Ali)
"""

from random import randint 
from random import choice as choose

NAME = "Imitator"
VERSION = 1.0
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
    "Bear":"A large, furry mammal that can be found in North America, Europe, and Asia.",
    "Monkey": "A small, furry mammal that has a long tail and lives in trees.",
    "Dolphin": "A marine mammal, related to whales and porpoises.",
    "Shark": "A large, predatory fish that has sharp teeth.",
    "Octopus": "A marine creature with eight arms and a beak.",
    "Spider": "An arthropod with eight legs and a body divided into two parts.",
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

ROLES = ["Imitator", "Not Imitator"]

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

def clr_scrn():
    '''clears screen by making new lines'''    
    print("\n"*7)


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
            if string[i] == " " or string[i] == "." or string[i] == ",":
                new_string += "\n"
            else:
                new_string += "-\n"
        

        new_string += string[i]
    result = "\n".join(new_string.strip().split("\n")).strip()
    result2 = []
    for i in result.split("\n"):
        result2.append(i.strip())


    return "\n".join(result2)


def warn(message, auto_break_lines = True, auto_break_lines_every= 20):
    '''Prints the given message ans waits for the user to press enter

    Args:
        message (str): the message to display
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.
    '''    
    clr_scrn()
    if auto_break_lines: input(add_line_breaks(message, auto_break_lines_every))
    else:input(message)
    clr_scrn()

def ask(question, ans=["yes","no"], auto_break_lines = True, auto_break_lines_every= 20):
    '''just like warn but instead asks the user for an input of number like choosing an option

    Args:
        question (str): the question to ask
        ans (list, optional): an list of all answers (recommended max: 3-4 answers). Defaults to ["yes","no"].
        auto_break_lines (bool, optional): if True the message will have a break line automatically each 20 letters. Defaults to True.

    Returns:
        _type_: _description_
    '''    
    while True:    
        clr_scrn()
        if auto_break_lines: print(add_line_breaks(question, auto_break_lines_every))
        else: print(question)

        print("-", end="")
        try: user_input = int(input("{}\n".format("\n-".join(ans))))
        except (ValueError,TypeError): continue

        try: user_input -= 1
        except TypeError: continue

        if user_input >= 0:
            clr_scrn()
            return ans[user_input]
        else:
            continue

def check_name(name, check_comma = True):
    if len(name) > 10 or len(name) <= 0:
        warn("Player name too long/ too short")
        return False

    try: players.index(name)
    except ValueError:pass # name not duplicate
    else:
        warn("name is duplicate")
        return False
        
    if check_comma:
        for i in list(name):
            if not i in PLAYER_NAME_ALLOWED_LETTERS:
                warn("Player not added. Name contained unallowed letters.")
                return False
    else:
        PLAYER_NAME_ALLOWED_LETTERS.append(",")
        for i in list(name):
            if not i in PLAYER_NAME_ALLOWED_LETTERS:
                warn("Player not added. Name contained unallowed letters.")
                PLAYER_NAME_ALLOWED_LETTERS.remove(",")
                return False       
        PLAYER_NAME_ALLOWED_LETTERS.remove(",")
    
    





no_of_questions = 5
players = []
PLAYER_NAME_ALLOWED_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

MAIN_MENU = """{0}
1.Add player
2.Play
3.Settings
----0:Quit----
""".format(NAME)
PLAYERS_MENU = """Plrs:{0}
-1.add 2.back 3.rmv-

"""
SETTINGS_MENU = """Settings
1.No. questions: {0}
2.Credits
----(0:cancel)----
""".format(no_of_questions)
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


while True:
    vote=[]
    invalid = False
    clr_scrn()
    user_input = int(input(MAIN_MENU))
    if user_input is False:continue
    if user_input == 0:
        clr_scrn()
        raise SystemExit("Quit")
    if user_input == 3:
        # settings
        user_input = int(input(SETTINGS_MENU))
        if user_input == 1:
            try:user_input = int(ask("number of questions to ask:", ["5", "10", "15", "20"]))
            except ValueError: continue
            no_of_questions = user_input
        elif user_input == 2:
            clr_scrn()
            warn(CREDITS_MENU, False)

            
    elif user_input == 1:
        # add player
        while True:
            clr_scrn()
            user_input = int(input(PLAYERS_MENU.format("\n".join(players))))
            if user_input == 2:
                break


            elif user_input == 3:
                clr_scrn()
                user_input = str(input(REMOVE_PLAYER_MENU.format(",\n".join(players))))
                if user_input == "1":
                    warn("Player name not\nremoved.\nPress EXE", False)
                    continue
                if user_input.find(","):
                    for i in user_input.split(","):
                        players.remove(i)
                        warn("removed player:\n{}".format(i))
                    continue
                else:
                    players.remove(i)
                    warn("removed player:\n{}".format(i))



            elif user_input == 1:
                clr_scrn()
                new_player_name = str(input(ADD_PLAYER_MENU)).strip().replace("  ", " ")
                if new_player_name == "1":
                    warn("Player name not\nadded.\nPress EXE", False)
                    continue
                if new_player_name == "1qa":
                    for i in ["DumOne","DumTwo", "DumThree"]:
                        players.append(i)
                    continue
                    
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
    elif user_input == 2:
        # play
        if len(players) <= 2:
            warn("Not enough players!")
            continue

        # the game
        catagory = randint(1,2)
        if catagory == 1:
            idea = choose((list(ANIMALS.keys())))
            definition = ANIMALS[idea]
        elif catagory == 2:
            idea = choose((list(FOODS.keys())))
            definition = FOODS[idea]

        


        Imitator = choose(players)

        for i in range(0,len(players)):
            warn("pass the device to {}".format(players[i]))
            warn(ROLE_MENU.format(players[i], "Imitator" if Imitator == players[i] else "Innocent", "idea is {}:".format(idea) if not Imitator == players[i] else "Try to guess idea"), False)
            if Imitator == players[i]:
                warn("Goodluck, try to ask questions that help identify idea")
            else:
                warn("definition of {0}:{1}".format(idea, definition),auto_break_lines_every = 20)
        
        for i in range(0, no_of_questions):
            while True:
                asker = choose(players)
                answerer = choose(players)
                if asker == answerer:
                    continue
                warn(QUESTION_MENU.format(i, no_of_questions, asker, answerer), False)
                break

        for i in range(0,len(players)):
            warn("pass the device to {}".format(players[i]))
            vote.append(ask("Who is imitating to\nunderstand the speech\nsubject?", players, False))
        warn("Time to reveal the\nimitator...\npress EXE to reveal", False)
        warn("The most voted player\nas imitator:\n{0}\nThe imitator was:\n{1}".format(max(set(vote), key=vote.count),Imitator), False)
        warn("Game finished")


            

    


