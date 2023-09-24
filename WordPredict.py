from random import choice as choose
from random import randint as random_number
DEBUG = False
words = ['car', 'ray', 'mix', 'sip', 'rot', 'pie', 'boy', 'toy', 'sky', 'beg', 'can', 'tug', 'end', 'bit', 'tax', 'mom', 'fit', 
'cow', 'dad', 'bat', 'two', 'day', 'sign', 'cook', 'mate', 'cork', 'wall', 'beer', 'ring', 'milk', 'mind', 'stir', 'step', 
'thaw', 'long', 'fall', 'jail', 'glue', 'pain', 'sock', 'kick', 'meal', 'rake', 'hand', 'rain', 'coal', 'self', 'drop',
'hunt', 'beds', 'oven', 'iron', 'melt', 'rest', 'sofa', 'deer', 'lake', 'part', 'view', 'lick', 'loss', 'camp', 'glow', 
'bolt', 'fire', 'army', 'comb', 'pail', 'join', 'miss', 'head', 'yard', 'moan', 'film', 'wail', 'wine', 'flow', 'aunt', 
'rule', 'face', 'cave', 'bear', 'stop', 'bone', 'wipe', 'tent', 'nail', 'week', 'land', 'fear', 'slip', 'walk', 'bump',
'look', 'frog', 'gaze', 'heat', 'boat', 'seed', 'pull', 'food', 'blow', 'list', 'tray', 'sack', 'unit', 'soup', 'fuel',
'dirt', 'worm', 'dogs', 'tale', 'name', 'chin', 'bell', 'hour', 'gate', 'grab', 'page', 'trip', 'live', 'form', 'last', 
'carve', 'blade', 'allow', 'metal', 'noise', 'paper', 'girls', 'cloth', 'slave', 'offer', 'order', 'shape', 'reply', 
'buyer', 'plant', 'touch', 'night', 'spoon', 'kneel', 'queen', 'grape', 'train', 'store', 'juice', 'chalk', 'stone', 
'doubt', 'point', 'verse', 'smell', 'skirt', 'shrug', 'drain', 'drink', 'quill', 'jelly', 'sense', 'trick', 'cover', 
'smash', 'smoke', 'cause', 'actor', 'chase', 'shelf', 'scent', 'brake', 'limit', 'sound', 'crook', 'stain', 'death', 
'month', 'songs', 'coach', 'laugh', 'level', 'mourn', 'force', 'bread', 'found', 'stove', 'guide', 'scarf', 'count', 
'trade', 'smile', 'place', 'twist', 'employ', 'aspect', 'people', 'sneeze', 'winter', 'bucket', 'flower', 'spring', 
'reason', 'degree', 'reduce', 'canvas', 'arrive', 'polish', 'cousin', 'advice', 'liquid', 'bottle', 'health', 'wander',
'belief', 'inform', 'amount', 'rescue', 'wonder', 'animal', 'shiver', 'cancer', 'reject', 'person', 'minute', 'mitten',
'remind', 'expert', 'chance', 'sample', 'poison', 'memory', 'sister', 'guitar', 'flavor', 'unlock', 'divide', 'wobble', 
'throne', 'escape', 'untidy', 'client', 'sticks', 'profit', 'wealth', 'change', 'bridge', 'hammer', 'attack', 'charge', 
'trains', 'pencil', 'porter', 'invent', 'supply', 'receipt', 'undress', 'weather', 'suggest', 'stretch', 'trainer', 
'pancake', 'purpose', 'library', 'support', 'fiction', 'history', 'applaud', 'morning', 'compete', 'develop', 'version', 
'compare', 'country', 'cushion', 'writing', 'concern', 'manager', 'opinion', 'radiate', 'creator', 'partner', 'imagine', 
'fireman', 'station', 'trouble', 'realize', 'fortune', 'society', 'courage', 'attempt', 'texture', 'disgust', 'holiday', 
'quality', 'provide', 'arrange', 'command', 'climate', 'kittens', 'impulse', 'science', 'control', 'cabbage', 'funeral',
'friction', 'creature', 'complain', 'accident', 'stranger', 'birthday', 'increase', 'instance', 'multiply', 'teaching',
'interest', 'response', 'stocking', 'notebook', 'chickens', 'building', 'reaction', 'election', 'business', 'memorize', 
'expansion', 'cigarette', 'knowledge', 'appliance', 'encourage', 'afternoon', 'existence', 'passenger', 'complaint', 
'territory', 'selection', 'newspaper', 'president', 'committee', 'inspector', 'treatment', 'apparatus', 'statement', 
'influence', 'education', 'basketball', 'instrument', 'wilderness', 'resolution', 'investment', 'reflection', 'punishment',
'toothpaste', 'suggestion', 'toothbrush', 'discussion', 'celebration', 'competition', 'observation', 'negotiation', 
'possibility', 'destruction', 'application', 'conversation', 'significance', 'distribution', 'establishment', 
'unaccountable', 'overconfident', 'psychological', 'environmental', 'disillusioned', 'comprehensive', 'entertainment', 
'lackadaisical', 'advertisement', 'communication', 'materialistic', 'knowledgeable', 'scintillating', 'heartbreaking', 
'differentiate', 'understanding', 'dysfunctional', 'sophisticated', 'administration', 'recommendation', 
'responsibility', 'transportation', 'administrative']

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


main_menu="""WORD PREDICT!
Level:{0} Pts:{3}
Pts req to lvl{1}:{2}
1.Start a new game
2.Settings
3.Quit game
OPTION NUMBER:"""
settings_menu="""SETTINGS|0 to quit
1.Show first letter: 
{0}
2.Show last letter: 
{1}
3.Next page
OPTION NUMBER:"""
settings_menu2="""SETTINGS|0 to quit
1.Guess tries:{0}
2.gradual difficulty:
{1}
3.Credits&Save
4.Load save
OPTION NUMBER:"""
credits_menu="""Credits
Developer:
blabla_lab
Version:1.2.1   #! MAINTAIN VERSION
Save code:
{1}
Words:{0}
PRESS EXE"""

def warn(text):
    print("\n")
    print(text)
    input("PRESS EXE")

def toggle(x):
    return not x

    

show_first_letter=True
show_last_letter=False
user_tries=6
points=0
points_for_level = 2
level = 0
gradual_difficulty=True
difficulty_word_length = 3 # this will be intial word length
def load_save():
    try:
        save_code=str(input("Save code:\n"))
        load_points = save_code.split(",")[:1]

        save_code_in_list_form=list(save_code.split(",")[1])
        print(save_code_in_list_form)
    except ValueError:
        warn("Only numbers in\nsave code, but I\nfound something thats\nnot a number")
    global points,level,user_tries,gradual_difficulty,show_first_letter,show_last_letter,points_for_level
    points=int(load_points[0])
    level=int(save_code_in_list_form[0])
    user_tries=int(save_code_in_list_form[1])
    gradual_difficulty = save_code_in_list_form[2] == "1"
    show_first_letter = save_code_in_list_form[3] == "1"
    show_last_letter = save_code_in_list_form[4] == '1'
    points_for_level=int(save_code.split(",")[2])
    print("load save")
    print(points,level,user_tries,gradual_difficulty,show_first_letter,show_last_letter,points_for_level)

tries=user_tries

def save(do_prompt=False):
    # variables used for save instead of using original value of orginal variable
    save_gradual_difficulty = 1 if gradual_difficulty is True else 0
    save_show_first_letter = 1 if show_first_letter is True else 0
    save_show_last_letter = 1 if show_last_letter is True else 0
    generated_save_code = "{0},{1}{2}{3}{4}{5},{6}".format(points,
        level,
        user_tries,
        save_gradual_difficulty,
        save_show_first_letter,
        save_show_last_letter,
        points_for_level)
    
    if do_prompt:
        warn("{0}\nwrite this in a paper".format(generated_save_code))
    else:
        return generated_save_code
    
while True:
    try:
        user_input = int(input(main_menu.format(int(level),int(int(level)+1),int(points_for_level)-int(points),int(points))))
        if user_input==3:
            break
        elif user_input==2:
            while True:
                user_input=int(input(settings_menu.format(show_first_letter,show_last_letter)))
                if user_input==0:
                    # quit
                    raise KeyError()
                elif user_input==1:
                    # show first letter
                    show_first_letter=toggle(show_first_letter)
                elif user_input==2:
                    # show last letter
                    show_last_letter=toggle(show_last_letter)
                elif user_input==3:
                    # next page
                    user_input=int(input(settings_menu2.format(user_tries,gradual_difficulty)))
                    if user_input==1:
                        user_tries=int(input("\n\nGuessing Tries\n(default:6,min:1,\nmax:9):\n\n"))
                        if user_input>9:
                            warn("You set\nGuessing Tries\nto more than 9\n\n\n")
                        elif user_input<=0:
                            warn("You set\nGuessing Tries\nto less than 1\n\n\n")
                        else:
                            tries=user_input
                    elif user_input==2:
                        gradual_difficulty=toggle(gradual_difficulty)
                    elif user_input==3:
                        input(credits_menu.format(len(words), save()))
                    elif user_input==4:
                        try:
                            load_save()
                        except IndexError:
                            warn("Wrong save code")
                    elif user_input==0:
                        continue

    except ValueError:
        warn("Only Numbers!")
        continue
    except KeyError:
        continue

    print("LOADING...\nTIP:\nYou can always\nend a game by\npressing 1\n\n")
    win=False
    #*levels require 3 points
    if points>=points_for_level:
        level += 1
        points_for_level = points_for_level * 2 + 1
        difficulty_word_length += 1

    if not gradual_difficulty:
        word = choose(words)
    elif gradual_difficulty is True:
        while True:
            word = choose(words)
            if len(word) <= difficulty_word_length:
                break
            else:
                continue



    tries=user_tries
    word_in_a_list_form = list(word)
    wrong_words_guessed = []
    guessing_list = ["_" for _ in word_in_a_list_form]
    if show_first_letter:
        guessing_list[0] = word_in_a_list_form[0]
    if show_last_letter:
        guessing_list[-1] = word_in_a_list_form[-1]


    while True:
        if win:
            break
        if DEBUG: print(word)
        print("Points:{0} Tries:{2}\nLevel:{1}\nPress 1 to quit game\n".format(points,level,tries,))
        print("".join(guessing_list))
        guess = str(input("Guess a letter:\n")).lower()

        if guess == "1":
            warn("YOU QUITED!\nThe word was\n{word}\n\n".format(word=word))
            break

        elif len(guess) > 1:
            warn("Only one letter")
        elif guess not in LETTERS:
            warn("You didnt type a letter!")

        if guess in word_in_a_list_form:
            indexes = [index for index in range(len(word_in_a_list_form)) if word_in_a_list_form[index] == guess]
            for i in indexes:
                guessing_list[i] = guess
            if guessing_list == word_in_a_list_form:
                warn("YOU DID IT!\nThe word was\n{word}\n\n".format(word=word))
                if tries == user_tries:
                    # no error while guessing
                    extra_points = random_number(1, len(word_in_a_list_form))
                    if extra_points == 0:extra_points = 1
                    points += extra_points
                    warn("You guessed the word\nwithout any tries!\nYou got extra {0}\npoint(s), Goodjob!".format(extra_points))

                win=True
                points+=1
                break
        else:
            print("WRONG")
            if tries <= 0:
                warn("YOU LOSE!\nThe word was\n{word}\n\n".format(word=word))
                break
            elif guess not in wrong_words_guessed:
                tries -= 1
                wrong_words_guessed.append(guess)
