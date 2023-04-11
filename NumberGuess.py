from random import randint
from math import ceil, floor

def warn(text):
    print("\n")
    print(text)
    input("PRESS EXE")

def percentage_of(value, total):
     return int(ceil((value / total)*100))

points_for_level = 1
points = 0
level = 0
math_range = 5
length = 2
guess_layout="""Guess the code!
Type A to quit

{0}

Hint:{2}
Number {1} is:"""

while True:
    level_progress_bar = []
    for i in range(0, floor(percentage_of(points, points_for_level)/20)+1):
            level_progress_bar.append("=")
    if points >= points_for_level:
        level += 1
        points_for_level += 5+level
        math_range +=1
        if not length > 20:
            length += 1


    level_progress_bar = "".join(level_progress_bar)
    main_layout="""NUMBER GUESS!
by blabla_lab
Level: {1}{2}{0}
Points: {3}
Press 1 then exe to
play""".format(
        level_progress_bar,
        level_progress_bar,
        level,
        points)
    try:
        user_input = int(input(main_layout))
    except ValueError:
        warn("Only numbers")
        continue
    # game #
    code=[]
    for i in range(0,length):
        code.append(str(randint(0,9)))
    no_number = 1

    guess_code = []
    for i in code:
        guess_code.append("_")

    # generate hint #
    def hint():
        print("Generating Hint...")
        while True:
            global result
            n1=randint(0,math_range)
            n2=randint(0,math_range)
            x=randint(1,3)
            if x == 1:
                result = "n1 - n2"
            elif x == 2:
                result = "n1 + n2" 
            elif x == 3:
                result = "n1 * n2"   
            # print(eval(result, globals(), locals()))
            if str(eval(result, {"points": points}, {"n1":n1, "n2":n2})) == code[no_number-1]:
                if x == 1:
                    return "{0}-{1}=?".format(n1,n2)
                elif x == 2:
                    return "{0}+{1}=?".format(n1,n2)
                elif x == 3:
                    return "{0}*{1}=?".format(n1,n2)

    # Guess
    while True:
        try:
            user_guess = str(input(guess_layout.format("".join(guess_code), no_number, hint())))    
            if user_guess == "A" or user_guess == "a":
                warn("YOU QUIT!\nThe code was:\n{}\nNo points earned".format("".join(code)))
                break
            elif int(user_guess) > 9:
                warn("only numbers\nbetween 1-9")
            elif user_guess == code[no_number-1]:
                guess_code[no_number-1] = str(user_guess)
                no_number+=1
            else:
                warn("YOU LOSE!\nThe code was:\n{}\nNo points earned".format("".join(code)))
                break
        except ValueError:
            warn("only numbers\nbetween 1-9")
        # check win
        if guess_code == code:
            warn("YOU WIN!\nThe code was:\n{}".format("".join(code)))
            points += 1
            break