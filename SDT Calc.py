input('SPEED&TIME,and\nDISTANCE\nCALCULATOR\nPress EXE to continue\nanywhere on\nthis program')
input("by:\nhttps://github.com/\nTejasKumar2009/\nSpeed-Calcu\nlator-Python\nPress EXE")

while(True):
    print("What to calculate?")
    try:
        calculator_options = int(input("\n0.Speed\n1.Time\n2.Distance\n"))
        if calculator_options==0:
            hours = int(input("Enter the Hours:\n"))
            minutes = int(input("Enter the Minutes:\n"))/60
            distance = float(input("Enter the distance\nin KM:\n"))

            time = hours+minutes
            speed = distance/time

            print("\nThe Average Speed of\nthe object in the\ntravel is:", round(speed), "\nKM/H",end="")
            input()
            break

        elif calculator_options==1:
            distance = float(input("Enter the\ndistance in KM:\n"))
            speed = float(input("Enter the speed\nin KM/H:\n"))

            time = distance/speed
            hours = int(time)
            minutes = round((time%1)*60)

            print("\nThe Time take by\nobject in the\ntravel is\n{}Hrs and\n{}Min".format(hours,minutes),end="")
            input()
            break


        elif calculator_options==2  :
            hours = int(input("Enter the Hours:\n"))
            minutes = int(input("Enter the Minutes:\n"))/60
            speed = float(input("Enter the\nspeed in KM/H:\n"))

            time = hours+minutes
            distance = round(speed*time, 1)

            print("\nThe Distance traveled\nby object is\n", distance, "KM",end="")
            input()
            break
        

        else:
            input("ERR\nONLY NUMBERS")
    except ValueError:
        input("ERR\nONLY NUMBERS")