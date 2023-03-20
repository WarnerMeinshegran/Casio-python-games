from random import randint



def ntt(x): # num to text
    x = int(x)
    if x == 1:
        return "rock"
    elif x == 2:
        return "paper"
    elif x == 3:
        return "scissors"

def result(x):
    print("cpu:", ntt(cc))
    print("you:", ntt(uc))
    print(x)

while True:
    try:
        uc = int(input("""1 = rock, 
2 = paper,
3 = scissors
4 = quit
choose a number:"""))
    except ValueError:
        print("NUMBERS ONLY!")
        continue
    cc = randint(1,3)

    if uc == cc:
        result("tie!")
    # win conditions for user
    elif uc == 1 and cc == 3:
        result("YOU WIN")
    elif uc == 2 and cc == 1:
        result("YOU WIN")
    elif uc == 3 and cc == 2:
        result("YOU WIN")
    #win condition for cpu
    elif uc == 3 and cc == 1:
        result("\nYOU LOSE\n")
    elif uc == 1 and cc == 2:
        result("\nYOU LOSE\n")
    elif uc == 2 and cc == 3:
        result("\nYOU LOSE\n")
    elif uc == 4:
        raise SystemExit("bye")
    else:
        print("ONLY NUMBERS BETWEEN\n(1~3)")
