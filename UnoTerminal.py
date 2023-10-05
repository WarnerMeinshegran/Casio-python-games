from random import choice as choose
import String_methodes as sm

"""
About:
a simple uno game but for calcs or terminal with bots support



Notes:
when you put a magic card like draw 4 and you choose color yellow
the next player will draw 4 cards
then the magic card will be replaced by a random normal yellow card
for the next player
"""

NAME = "UnoTerminal"
VERSION = "1.1"
CREATION_DATE = "7/July/2023"


YELLOW = ['1 Yellow', '2 Yellow', '3 Yellow', '4 Yellow', '5 Yellow', '6 Yellow', '7 Yellow', '8 Yellow', '9 Yellow', "Draw 2 Yellow", "Wild Yellow", "Skip Yellow", "Draw 4 Yellow"]
RED = ['1 Red', '2 Red', '3 Red', '4 Red', '5 Red', '6 Red', '7 Red', '8 Red', '9 Red', 'Draw 2 Red', "Wild Red", "Skip Red", "Draw 4 Red"]
BLUE = ['1 Blue', '2 Blue', '3 Blue', '4 Blue', '5 Blue', '6 Blue', '7 Blue', '8 Blue', '9 Blue', 'Draw 2 Blue', "Wild Blue" , "Skip Blue", "Draw 4 Blue"]
GREEN = ['1 Green', '2 Green', '3 Green', '4 Green', '5 Green', '6 Green', '7 Green', '8 Green', '9 Green', 'Draw 2 Green', "Wild Green", "Skip Green", "Draw 4 Green"]

YELLOW_NO_MAGIC = ['1 Yellow', '2 Yellow', '3 Yellow', '4 Yellow', '5 Yellow', '6 Yellow', '7 Yellow', '8 Yellow', '9 Yellow']
RED_NO_MAGIC = ['1 Red', '2 Red', '3 Red', '4 Red', '5 Red', '6 Red', '7 Red', '8 Red', '9 Red']
BLUE_NO_MAGIC = [ '1 Blue', '2 Blue', '3 Blue', '4 Blue', '5 Blue', '6 Blue', '7 Blue', '8 Blue', '9 Blue']
GREEN_NO_MAGIC = ['1 Green', '2 Green', '3 Green', '4 Green', '5 Green', '6 Green', '7 Green', '8 Green', '9 Green']




MAGIC_CARDS = ["Draw 2 Yellow", "Draw 2 Red", "Draw 2 Blue", "Draw 2 Green" , "Draw 4", "Wild Card"]

UNO_CARDS = YELLOW + RED + BLUE + GREEN

UNO_CARDS_TO_GIVE = YELLOW_NO_MAGIC + RED_NO_MAGIC + BLUE_NO_MAGIC + GREEN_NO_MAGIC


cards_per_player = 4
assist_players = True
draw_until_matching_card = False # draws a card until a correct one is found, after that it will play it automatically
# cancel_magic_using_skip = True

players = []
bots_count = 1
played_card = None
placed_card = None

PLAYER_NAME_ALLOWED_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


MAIN_MANU = """{Name}!
1-Play
2-Settings
3-Players
0-Quit
--Type a number--
""".format(Name=NAME)

# SETTINGS_MENU = """Settings|0 to quit
# 1-Credits
# 2-Cards per player:
# {Cards_per_player}
# 3-
# --Type a number--
# """

#! make settings for your features here!
SETTINGS = {
    #* "option" : ["<Variable>", "<Type: int or bool>", "<If type is Int then supply min max in this format: min-max>"]

    "Cards per player" : ["cards_per_player", "int", "4-15"],
    "Draw till playable" : ["draw_until_matching_card", "bool"],
    "Recommend Cards" : ["assist_players", "bool"]

}


SETTINGS_TOGGLE_MENU = """Settings|0 to quit
{Item}:
  {State}
-1:Disable|2:Enable-
"""

ADD_PLAYER_MENU = """Whats the name
of the player you
want to add?
seperate names by ','
to batch add names
-(1:cancel)-
"""
PLAYERS_MENU = """Manage players
1.Add 
2.Back 
3.Remove
4.View players 
5.Add bot
"""

SETTINGS_SLIDER_MENU = """Settings|a to quit
{Item}:
{Value}

Type a number between
{Min}-{Max}
-----------"""

CREDITS_MENU = """Credits
{Name} {Version}
Made by blabla_lab
{Random_card}
""".format(Name=NAME, Version=VERSION, Random_card=choose(MAGIC_CARDS))


def check_name(name, check_comma = True):
    if len(name) > 9 or len(name) <= 0:
        sm.warn("Player name too long/ too short. max. 9 letters and min.1 letter")
        return False

    if name.find("CPU") != -1:
        sm.warn("You cant use the name CPU, its reserved for bots")


    try: players.index(name)
    except ValueError:pass # name not duplicate
    else:
        sm.warn("name is duplicate")
        return False

    if check_comma:
        for i in list(name):
            if i not in PLAYER_NAME_ALLOWED_LETTERS:
                sm.warn("Player not added. Name contained unallowed letters.")
                return False
    else:
        PLAYER_NAME_ALLOWED_LETTERS.append(",")
        for i in list(name):
            if i not in PLAYER_NAME_ALLOWED_LETTERS:
                sm.warn("Player not added. Name contained unallowed letters.")
                PLAYER_NAME_ALLOWED_LETTERS.remove(",")
                return False
        PLAYER_NAME_ALLOWED_LETTERS.remove(",")
    
def most_common(list):
    return max(list, key=list.count)


def average_cards_color(player):
    x = []
    for card in player_cards[player]:
        x.append(card.split(" ")[-1])
    # print("DEBUG x:{}".format(x))
    x = most_common(x)
    # print("DEBUG:most common {}".format(x))
    return x

def draw(amount, player, silent = False):
    '''give a player cards

    Args:
        amount (int): amount of cards to give
        player (str): give cards to this player
        silent (bool, optional): doesnt not print informative messges(i.e: X draw a card). Defaults to False.
    returns: last drawn card
    '''    


    if player.find("CPU") != -1:bot = True
    else: bot = False

    for i in range(amount):
        s = choose(UNO_CARDS_TO_GIVE+MAGIC_CARDS)

        if not silent and not bot:
            sm.warn("Card {0} out of {1}\n{3} got {2}\n".format(i+1,amount,s,player))
        elif bot and not silent: sm.warn("{} drew {}/{} card(s)\n".format(player,i+1,amount), clear_screen=False)
        player_cards[player].append(s)
    return s

def draw_until_correct_card(player, bots = False):
    global placed_card, played_card
    sm.clr_scrn()
    while True:
        drawn_card = draw(1, player=player, silent=False)
        # input("Drawn card:{0}\nPlaced card:{1}\nIs it playable?\n{2}".format(drawn_card, placed_card, "Yes" if check_if_played_card_is_correct(card=drawn_card) is True else "No"))

        played_card = drawn_card
        if check_if_played_card_is_correct(card=drawn_card) is True:
            if played_card.startswith("Wild") or played_card.startswith("Draw 4"):
                if not bots:
                    color = sm.ask("pick a color for {}".format(played_card), ["Red","Blue","Green","Yellow"], prompt=False)
                else:
                    color = choose(["Red","Blue","Green","Yellow"])
                placed_card = "{0} {1}".format(played_card, color)
            else:                  
                placed_card = played_card

            break


def remove_card(card):
    global exit_loop
    player_cards[player].remove(card)
    # if player has no cards
    if player_cards[player] == []:
        sm.warn("The winner is {}".format(player))
        exit_loop = True
        

def check_if_played_card_is_correct(card = None):
    # check system
    if card is None: card = played_card

    if card == "Wild Card": return True
    elif card.startswith("Draw 2"):
        placed_card_color = placed_card.split(" ")[1]
        if card.endswith("Yellow") and placed_card_color == "Yellow":
            return True
        elif card.endswith("Red") and placed_card_color == "Red":
            return True
        elif card.endswith("Blue") and placed_card_color == "Blue":
            return True
        elif card.endswith("Green") and placed_card_color == "Green":
            return True

    
    played_card_number = card.split(" ")[0]
    played_card_color =  card.split(" ")[1]
    placed_card_number = placed_card.split(" ")[0]
    placed_card_color =  placed_card.split(" ")[1]
    
    if played_card_number == placed_card_number: return True
    elif played_card_color == placed_card_color: return True
    elif played_card_number == "Draw" and played_card_color == "4": return True
    else: return False
    


def replace_magic_card_with_normal_card_of_same_color(card):
    if card.find("Yellow") != -1:return choose(YELLOW_NO_MAGIC)
    elif card.find("Red") != -1:return choose(RED_NO_MAGIC)
    elif card.find("Blue") != -1:return choose(BLUE_NO_MAGIC)
    elif card.find("Green") != -1:return choose(GREEN_NO_MAGIC)
    else:
        print("""
ERROR: replace_magic_card_with_normal_card_of_same_color
card: {0}
placed_card: {1}
checks:
Yellow: {2}
Red: {3}
Blue: {4}
Green: {5}""".format(card,placed_card, True if card.find("Yellow") != -1 else False, True if card.find("Red") != -1 else False, True if card.find("Blue") != -1 else False, True if card.find("Green") != -1 else False))
        raise ValueError



def add_player(player):
    players.append(player)

def remove_player(player):
    players.remove(player)
    if user_input.find("CPU") == -1:
        sm.warn("Removed player:\n{}".format(user_input))
    else:
        sm.warn("Removed bot:\n{}".format(user_input))
        bots_count -= 1




while True:
    sm.clr_scrn()
    user_input = input(MAIN_MANU)
    if user_input == "0":break
    elif user_input == "2":
        # settings
        sm.clr_scrn()
        user_input = sm.view_list(list(SETTINGS.keys()), pick_confirm=False, title="--Settings--")
        sm.clr_scrn()
        for option in SETTINGS:
            if user_input == option:
                option_variable = SETTINGS[option][0]
                option_type = SETTINGS[option][1]
                if option_type == "int":
                    option_min_max = SETTINGS[option][2].split("-")
                    user_input = input(SETTINGS_SLIDER_MENU.format(Item=option, 
                                                            Value=globals()[option_variable], 
                                                            Min=option_min_max[0], 
                                                            Max=option_min_max[1]))
                    try:
                        if int(user_input) >= int(option_min_max[0]) and int(user_input) <= int(option_min_max[1]):
                            exec("{} = {}".format(option_variable, int(user_input)))
                    except ValueError:continue

                elif option_type == "bool":
                    user_input = input(SETTINGS_TOGGLE_MENU.format(Item = option, State = globals()[option_variable]))
                    if user_input == "1":exec("{} = {}".format(option_variable, "False"))
                    if user_input == "2":exec("{} = {}".format(option_variable, "True"))
        continue

    elif user_input == "3":
        # player setup
        sm.clr_scrn()
        user_input = input(PLAYERS_MENU.format(sm.add_line_breaks(",".join(players))))
        if user_input == "1":
            # add player
            sm.clr_scrn()
            user_input = input(ADD_PLAYER_MENU)
            if user_input == "1":continue
            elif user_input == "1qa":
                add_player("Dummy")
                players.append("CPU {}".format(bots_count))
                sm.warn("Added bot:\n{} !".format("CPU {}".format(bots_count)))
                bots_count += 1   
                continue
            if user_input.find(",") != -1:
                for name in user_input.split(","):
                    if check_name(name) is False:
                        continue
                    else:
                        add_player(name)
                        sm.warn("Added player:\n{}".format(name))
            else:
                if check_name(user_input) is False:
                    continue
                else: 
                    add_player(user_input)
                    sm.warn("Added player:\n{}".format(user_input))
        elif user_input == "2":continue
        elif user_input == "3":
            sm.clr_scrn()
            user_input = sm.view_list(players, title="-Remove player-")
            try:players.index(user_input)
            except ValueError:sm.warn("Player not found")
            else:
                remove_player(user_input)

            finally:continue
        elif user_input == "4":
            sm.clr_scrn()
            sm.view_list(players, readonly=True, title="--Players--")
        elif user_input == "5":
            players.append("CPU {}".format(bots_count))
            sm.warn("Added bot:\n{} !".format("CPU {}".format(bots_count)))
            bots_count += 1     
        elif user_input == "vmb": # (v)ery (m)any (b)ots    
            print("---DEBUG---")
            for i in range(int(input("Number of bots to add"))):
                players.append("CPU {}".format(bots_count))
                bots_count += 1   
            sm.warn("done")

        continue
        


        


    #* Game
    if user_input != "1":
        continue
    else:
        if len(players) < 2:
            sm.warn("Need at least 2 players to start game.")
            continue


    # Prepare cards
    sm.clr_scrn()
    print("Preparing cards...")
    player_cards = {}
    for i in players:
        player_cards[i] = [choose(UNO_CARDS_TO_GIVE+MAGIC_CARDS) for x in range(cards_per_player)]


    magic_color = None # used for black magic cards

    sm.clr_scrn()

    # view cards
    for player in players:
        while True:
            if player.find("CPU") == -1:
                input("give device\nto {}".format(player))
                if sm.ask("Are you {}?\n".format(player), ["yes","no"], prompt=False) == "no":
                    continue
                sm.warn("click exe to view your cards,NEVER show your cards!".format(player))
                sm.view_list(player_cards[player], readonly=True, title = "--Cards--")
            else:
                sm.warn("{} has saw its cards\npress exe to continue".format(player))
                
            break

    while True:
        placed_card = choose(UNO_CARDS)
        if placed_card.startswith("Draw 2") or placed_card.startswith("Draw 4") or placed_card.startswith("Wild") or placed_card.startswith("Skip"):continue
        else:break


    # play
    human_players = []
    for i in players:
        if i.find("CPU") == -1:
            human_players.append(i)
        
        
    exit_loop = False
    while exit_loop is False:
        for player in players:
            
            if exit_loop is True:break

            bot_turn = True if player.find("CPU") != -1 else False

            if bot_turn is False and len(human_players) != 1: # if there is 1 human player stop asking to pass device to him / her
                input("give device\nto {}".format(player))
                if sm.ask("Are you {}?".format(player), ["yes","no"]) == "no":continue
            elif bot_turn is True:
                print(sm.add_line_breaks("{} is playing".format(player)))
            elif bot_turn is False and len(human_players) == 1:
                sm.warn("Its your turn\n{}".format(player), auto_break_lines=False)

            if placed_card.startswith("Draw 2"):
                sm.warn("The placed card is {}".format(placed_card))
                draw(2, player)
                placed_card = replace_magic_card_with_normal_card_of_same_color(placed_card)
            elif placed_card.startswith("Draw 4"):
                sm.warn("The placed card is {}".format(placed_card))
                draw(4, player)
                placed_card = replace_magic_card_with_normal_card_of_same_color(placed_card)
            elif placed_card.startswith("Skip"):
                if not bot_turn:sm.warn("YOU ARE SKIPPED")
                elif bot_turn:sm.warn("{} is skipped".format())
                placed_card = replace_magic_card_with_normal_card_of_same_color(placed_card)
            elif placed_card.startswith("Wild"):
                placed_card = replace_magic_card_with_normal_card_of_same_color(placed_card)

            if bot_turn:
                print(sm.add_line_breaks("The placed card is {}. {} is thinking...".format(placed_card, player)))
                #! BOT AI

                if placed_card in player_cards[player]:
                    # bot has exact card in inventory 
                    played_card = player_cards[player][player_cards[player].index(placed_card)]


                    remove_card(played_card)
                    placed_card = played_card
                    print("{}\nchose\n{}".format(player,placed_card))
                    
                else:
                    """
                    Advanced check

                    How does it work:
                    The system basically chooses a card from the 
                    inventory starting from the first to last,
                    then it sets this choosen card as a played card and runs the check system
                    which is a function named check_if_played_card_is_correct()
                    if the function returned true i will laye this card else it will choose the next card untill
                    it goes to the last one. if nothing is correct the CPU will draw a card
                    """
                    CPU_inventory = player_cards[player]
                    bot_tries = 0
                    while True:
                        try:
                            played_card = CPU_inventory[bot_tries]
                        except IndexError:
                            draw(1, player, True)
                            # input("{} drew a card".format(player))
                            break
                        # input("DEBUG:\n{bot} choose {card}".format(bot=player, card=played_card))
                        correct = check_if_played_card_is_correct()
                        # input("DEBUG:\nplayed card:\n{}\nplaced card:\n{}\nCorrect:\n{}".format(played_card, placed_card, correct))
                        if correct is False: 
                            # print("bot tries: {}".format(bot_tries))

                            if bot_tries > len(player_cards[player]):
                                # tried too much
                                if draw_until_matching_card: draw_until_correct_card(player, )
                                else: draw(1, player, )
                                # input("{} drew a card".format(player))
                                break

                            bot_tries +=1
                            continue
                        if correct:
                            print(sm.add_line_breaks("{} played {}".format(player, played_card))) 
                            remove_card(played_card)
                            # black magic cards
                            if played_card.startswith("Draw 4"):
                                magic_color = average_cards_color(player)
                                # print("DEBUG: avg color: {}".format(magic_color))
                                played_card = "Draw 4 {}".format(magic_color)
                            elif played_card.startswith("Wild"):
                                magic_color = average_cards_color(player)
                                # print("DEBUG: avg color: {}".format(magic_color))
                                played_card = "Wild {}".format(magic_color)

                            placed_card = played_card
                            # input("DEBUG: {} played corrrectly".format(player))
                            break
                
                            
                input("{} is done\n".format(player))

                continue

            if not bot_turn:
                assist_players_suggestion = None
                for card in player_cards[player]:
                    if check_if_played_card_is_correct(card=card) is True:
                        assist_players_suggestion = "Play a card"
                        break
                    else:
                        assist_players_suggestion = "Draw a card"

                user_input = sm.ask("The placed card is \n{0}{1}".format(placed_card, "\nRecommend action:\n{}".format(assist_players_suggestion) if assist_players else ""), ["Draw a card", "Play a card"], prompt=False, auto_break_lines=False)
    
                if user_input == "Play a card":
                    played_card = sm.view_list(player_cards[player], pick_confirm_question="Play {}?", title="placed card:{}".format(placed_card))


                    correct = check_if_played_card_is_correct()
                    
                    if correct:
                        remove_card(played_card)


                        if played_card.startswith("Wild") or played_card.startswith("Draw 4"):
                            color = sm.ask("pick a color for {}".format(played_card), ["Red","Blue","Green","Yellow"], prompt=False)
                            placed_card = "{0} {1}".format(played_card, color)
                        else:                  
                            placed_card = played_card

                        continue
                    else:
                        input("You cant play this\ncard! You will\ndraw a card")
                        if draw_until_matching_card: draw_until_correct_card(player)
                        else: draw(1, player)

                    

                        continue
                else:
                    sm.warn("Press EXE to DRAW a card")
                    if draw_until_matching_card: draw_until_correct_card(player)
                    else: draw(1, player)
