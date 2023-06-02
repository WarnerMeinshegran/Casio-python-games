from random import choice as choose
from random import randint

# change this to big number if your calc is faster than fx-9860giii
WAIT_TIME = 800 # this should take one second.
# ^^^ for no fake loading set this to one 

AI_question_list=["go to university?","spend lesstime on\nsocial media?",
"start eating\nhealthy food?","social media is bad",
"take that many\nsubjects in school?","wear a uniform when\nwe go to school?",
"pay a lot of money to\nget better education?","pay taxes?","study languages?",
"study Math?","pretend you\ndon't need help?","you afraid of\nmaking mistakes?",
"cats hate cucumbers?","athletes get a\nlot of money?","you hate reading\nbooks?",
"glue doesnt stick\ninside the bottle","pizzas are round but\nnot there boxes?",
"do you like\nspicy food?","musics are soothing?","do you want to\nbe successful?",
"teachers are\nalways right","you stay too much\non your phone",
"schools were invented","iPhones are\nexpensive?", "android is good?", "you are stupid?", "you are nerd?"]
AI_answer_list=["it's important",
"it makes difference",
"we need to suffer",
"I'm bored",
"I can't think reason",
"I'm feeling generous",
"I'm a good sport",
"I have nerd powers",
"I can.",
"why not?",
"it's funny.",
"it's stupid.",
"it's pointless.",
"it's a waste of time",
"I don't care",
"I'm crazy",
"I'm weird",]
main_menu="""
Why? Because.
1.Start Game
2.How to play
3.Quit
Type option number:
"""
how_to_menu1="""How to play
Start by typing 
a question thats 
starts with why, 
then pass the 
calculator to the"""
how_to_menu2="""next player who will
type an answer that
starts with why, 
without looking at 
the question.
Finally the game"""
how_to_menu3="""will display both
the question and
answer, so you
can see the funny
answer to the 
question asked"""
gamemode_menu="""
GAMEMODE
1.One player
2.Two player
Type option number:
"""
question_menu="""
Its your turn to 
type a question,
your question should 
start with why.
question:Why
"""
answer_menu="""
Its your turn to 
type the answer,
your answer will 
start with because.
answer:Because,
"""
reveal_menu="""Why
{0}
Because,
{1}
Press EXE to
continue"""

def warn(text):
    print("\n")
    print(text)
    input("EXE TO CONTINUE")

while True:
    try:
        user_input=int(input(main_menu))
    except ValueError:
        warn("Only numbers\nbetween 1~3")
    if user_input==1:
        try:
            # Game mode
            gamemode=int(input(gamemode_menu))   
            if gamemode>2:
                raise ValueError     
        except ValueError:
            warn("Only number\n1 and 2")
        else:
            if gamemode==1:
                # Singleplayer
                '''
                Ai will basiclly just pick a 
                random question/ answer
                from a list and then the player 
                will have to answer.
                '''
                if randint(1,2) == 1:
                    question=choose(AI_question_list)
                    print("\n\n\nAI is thinking\n of a question..") # i made this fake loading so players know what the ai is doing.
                    for i in range(0, WAIT_TIME*2):
                        pass
                    answer=str(input(answer_menu))
                else:
                    question=str(input(question_menu))
                    print("\n\n\nAI is thinking\nof a answer..")
                    for i in range(0, WAIT_TIME*2):
                        pass
                    answer=choose(AI_answer_list)
                input("\nIts now time\nto display both\nquestion and\nanswer!\npress EXE to\nreveal...")
                input(reveal_menu.format(question,answer))
                continue
            elif gamemode==2:
                question=str(input(question_menu))
                answer=str(input(answer_menu))
                input("\nIts now time\nto display both\nquestion and\nanswer!\npress EXE to\nreveal...")
                input(reveal_menu.format(question,answer))
                continue
        
    elif user_input==2:
        # how to play
        warn(how_to_menu1)
        warn(how_to_menu2)
        warn(how_to_menu3)
        continue
    elif user_input==3:
        raise SystemExit(0)
