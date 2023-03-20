from random import choice as choose
words = ['gate', 'history', 'stove', 'station', 'verse', 'selection', 'stretch', 'cow', 'kittens', 'rule', 
'metal', 'heat', 'birthday', 'blade', 'hand', 'walk', 'territory', 'spring', 'afternoon', 'frog', 
'noise', 'creator', 'bottle', 'toy', 'worm', 'self', 'oven', 'rest', 'purpose', 'limit', 'dirt', 
'pancake', 'smoke', 'seed', 'army', 'boy', 'friction', 'yard', 'pull', 'country', 'meal', 
'society', 'aunt', 'girls', 'car', 'observation', 'pail', 'ring', 'scarf', 'trains', 'suggestion', 
'form', 'pencil', 'coal', 'texture', 'drain', 'receipt', 'liquid', 'deer', 'chalk', 'porter', 
'statement', 'impulse', 'person', 'business', 'loss', 'trick', 'touch', 'sack', 'cabbage', 
'wilderness', 'partner', 'competition', 'instrument', 'minute', 'holiday', 'mitten', 
'morning', 'poison', 'stone', 'hammer', 'end', 'pie', 'knowledge', 'mind', 'dad', 'fire', 
'morning', 'winter', 'fireman', 'step', 'sticks', 'chin', 'grape', 'can', 'rake', 'spoon', 
'treatment', 'weather', 'death', 'porter', 'queen', 'tent', 'look', 'bone', 'shelf', 'amount', 
'bat', 'beds', 'sock', 'advertisement', 'blow', 'chickens', 'wall', 'toothpaste', 'flavor', 
'noise', 'lake', 'ray', 'fear', 'memory', 'skirt', 'bucket', 'bridge', 'basketball', 'bear', 
'crook', 'toothbrush', 'cause', 'cover', 'train', 'reaction', 'fuel', 'quill', 'dogs', 'unit', 
'library', 'chance', 'scent', 'guide', 'committee', 'sign', 'degree', 'slave', 'creature', 
'advice', 'iron', 'week', 'sofa', 'trade', 'country', 'health', 'shape', 'sneeze', 'wealth', 
'land', 'tray', 'smoke', 'cave', 'boat', 'stocking', 'person', 'notebook', 'bell', 'rain', 'bit', 
'actor', 'animal', 'drop', 'throne', 'smash', 'songs', 'appliance', 'sound', 'coach', 'day', 
'cushion', 'juice', 'month', 'verse', 'thaw', 'arrive', 'attempt', 'employ', 'glow', 'order', 
'realize', 'mate', 'untidy', 'arrange', 'face', 'complain', 'last', 'milk', 'multiply', 'live', 
'bat', 'rescue', 'found', 'brake', 'film', 'compete', 'name', 'sip', 'mix', 'count', 'escape', 
'bump', 'kneel', 'mourn', 'plant', 'join', 'grab', 'rot', 'comb', 'stain', 'shiver', 'store', 
'bolt', 'beg', 'glue', 'miss', 'remind', 'chase', 'list', 'nail', 'stir', 'offer', 'jail', 
'imagine', 'interest', 'develop', 'command', 'long', 'reply', 'head', 'applaud', 'divide', 
'wipe', 'invent', 'attack', 'place', 'compare', 'carve', 'tug', 'allow', 'wander', 'shrug', 
'melt', 'gaze', 'lick', 'fit', 'unlock', 'flow', 'reject', 'charge', 'supply', 'concern',
'undress', 'inform', 'wonder', 'provide', 'flower', 'suggest', 'camp', 'wobble', 'smell', 
'influence', 'wail', 'kick', 'radiate', 'support', 'reduce', 'increase', 'hunt', 'trip', 'moan', 
'point', 'memorize', 'encourage', 'understanding', 'communication', 'recommendation',
'administration', 'entertainment', 'responsibility', 'transportation', 'establishment', 
'differentiate', 'unaccountable', 'knowledgeable', 'disillusioned', 'environmental', 
'heartbreaking', 'dysfunctional', 'psychological', 'sophisticated', 'lackadaisical', 
'materialistic', 'administrative', 'overconfident', 'comprehensive', 'scintillating',
'education', 'sense', 'person', 'apparatus', 'level', 'mind', 'cook', 'twist', 'impulse',
'night', 'trouble', 'doubt', 'expert', 'profit', 'opinion', 'hour', 'canvas', 'destruction', 
'stretch', 'smoke', 'soup', 'existence', 'discussion', 'guide', 'limit', 'trick', 'wine', 
'jelly', 'quality', 'polish', 'stop', 'drink', 'manager', 'cloth', 'sky', 'change', 
'punishment', 'tax', 'food', 'laugh', 'fall', 'expansion', 'belief', 'support', 'fiction', 
'slip', 'cork', 'view', 'reason', 'force', 'form', 'bread', 'disgust', 'order', 'page', 
'building', 'smile', 'part', 'pain', 'competition']

main_menu="""WORD PREDICT!
Level:{0}
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
3.Credits
4.Previous page
OPTION NUMBER:"""
credits_menu="""Credits
Developer:
blabla_lab
Words generated by: 
randomlists.com
Current words in game
{0}"""

def warn(text):
    print("\n")
    print(text)
    input("PRESS EXE")

def toggle(x):
    if x:
        return False
    else:
        return True

show_first_letter=True
show_last_letter=False
user_tries=6
tries=user_tries
points=0
points_for_level = 3
level = 0
gradual_difficulty=True
difficulty_word_length = 3 # this will be intial word length
while True:
    try:
        user_input = int(input(main_menu.format(level,int(level+1),points_for_level-points)))
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
                        user_tries=int(input("\n\nGuessing Tries\n(default:6,min:1,\nmax:20):\n\n"))
                        if user_input>20:
                            warn("You set\nGuessing Tries\nto more than 20\n\n\n")
                        elif user_input<=0:
                            warn("You set\nGuessing Tries\nto less than 1\n\n\n")
                        else:
                            tries=user_input
                    elif user_input==2:
                        gradual_difficulty=toggle(gradual_difficulty)
                    elif user_input==3:
                        input(credits_menu.format(len(words)))
                    elif user_input==0:
                        continue
                
    except ValueError:
        warn("Only Numbers!")
        continue
    except KeyError:
        continue

    print("LOADING...\nYou can always\nend a game by\npressing 1\n\n\n")
    win=False
    #*levels require 3 points and then gradualy +1 point every time
    if points==points_for_level:
        level += 1
        points_for_level +=1


    if not gradual_difficulty:
        word = choose(words)
    elif gradual_difficulty is True:
        difficulty_word_length += points#determines the legth of the word, increase with levels, levels increase with points.
        while True:
            word = choose(words)
            if len(word) <= difficulty_word_length:
                break
            else:
                continue
            
            
    
    tries=user_tries
    word_in_a_list_form=[]
    for i in word:
        word_in_a_list_form.append(i)
    guessing_list = []
    wrong_words_guessed = []
    for i in word_in_a_list_form:
        guessing_list.append("_")
    if show_first_letter:
        guessing_list[0] = word_in_a_list_form[0]
    if show_last_letter:
        guessing_list[-1] = word_in_a_list_form[-1]


    while True:
        if win:
            break
        print("Points:{0}\nTries:{2}\nLevel:{1}\n".format(points,level,tries,))
        print("".join(guessing_list))
        guess = str(input("Guess a letter:\n")).lower()

        # error checking
        if guess == "1":
            warn("YOU QUITED!\nThe word was\n{}\n\n".format(word))
            break
        elif len(guess) > 1:
            warn("Only one letter")
        elif guess.isdigit():
            warn("type a word,\nnot a digit!")
        
        if guess in word_in_a_list_form:
            # for i, j in enumerate(word_in_a_list_form):
            #     if j == guess:
            #         guessing_list[i] = guess
            #         if guessing_list == word_in_a_list_form:
            #             warn("YOU DID IT!\nThe word was\n{}\n\n".format(word))
            #             win=True
            #             break
            indexes = [index for index in range(len(word_in_a_list_form)) if word_in_a_list_form[index] == guess]               
            for i in indexes:
                guessing_list[i] = guess
            if guessing_list == word_in_a_list_form:
                warn("YOU DID IT!\nThe word was\n{}\n\n".format(word))
                win=True
                points+=1
                break
        else:
            print("WRONG")
            if tries <= 0:
                warn("YOU LOSE!\nThe word was\n{}\n\n".format(word))
                break
            elif not tries <=0 and not guess in wrong_words_guessed:
                tries -= 1
                wrong_words_guessed.append(guess)