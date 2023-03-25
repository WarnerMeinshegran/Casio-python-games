#slpe to standard form
try:
    while True:
        input("Slope to standard\nform\ny=x+b\nAC to quit\nEXE to start")
        try:
            x=int(input("What's the value of x\n"))
            init=int(input("What's the\ny-intercept?\n"))
        except ValueError:
            input("\nOnly integers please\nEXE to continue")
            continue
        else:
            try:
                #detect if x is negative
                x_negative=False
                y_negative=False
                if x < 0:
                    x_negative = True
                if init < 0:
                    y_negative = True
                #make equation
                eq = None
                if y_negative:
                    eq="y={0}x{1}".format(x, init)
                    print(eq)
                else:
                    eq="y={0}x+{1}".format(x, init)
                    print(eq)
                if x_negative:
                    print("x is negative")
                if y_negative:
                    print("y-intercept is\nnegative")
                if int(input("Is this correct?\n1=yes,2=no\n")) == 2:
                    continue
                #convert
                if not x_negative and not y_negative:
                    eq="{0}x-y=-{1}".format(x, init)
                    print("\nThe answer is:")
                    print(eq)
                    input("EXE to continue")
                elif x_negative and y_negative:
                    x=x*-1
                    eq="{0}x+y={1}".format(x, init)
                    print("\nThe answer is:")
                    print(eq)
                    input("EXE to continue")
                elif not x_negative and y_negative:
                    init=init*-1
                    eq="{0}x-y={1}".format(x, init)
                    print("\nThe answer is:")
                    print(eq)
                    input("EXE to continue")
                elif x_negative and not y_negative:
                    x=x*-1
                    eq="{0}x+y={1}".format(x, init)
                    print("\nThe answer is:")
                    print(eq)
                    input("EXE to continue")

            except ValueError:
                input("\nOnly integers please\nEXE to continue")
                continue
except KeyboardInterrupt:
    print("\n\nAPP QUIT\nKEYBOARD\nINTERRUPT\n")