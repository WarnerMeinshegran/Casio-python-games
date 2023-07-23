import String_methodes as sm
from random import choice as choose
options = {"Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper"}
sm.warn("Press exe to play rock paper scissors against a bot")
while True:
    user_input = sm.view_list(list(options.keys()), pick_confirm=False, title="-choose something-")
    bot = choose(list(options.keys()))
    sm.warn("You:{you}\nBot:{bot}".format(you = user_input, bot = bot))
    if user_input == bot:sm.warn("Draw")
    elif user_input in options[bot]:sm.warn("Lose")
    else:sm.warn("Win")
