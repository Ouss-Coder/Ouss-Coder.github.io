while True:
    try:
        n1 = float(input("Enter first number: "))
        o = input("Enter your operasion: ")
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("please Enter real number \n . \n . \n . ")
    else:
        if o == "+":
            print(n1 + n2)
            c = input("if want to stop print any thing or press ENTER, if no print yes: ")
            if c == "yes":
                continue
            else:
                break
        elif o == "-":
            print(n1 - n2)
            c = input("if want to stop print any thing or press ENTER, if no print yes: ")
            if c == "yes":
                continue
            else:
                break
        elif o == "*":
            print(n1 * n2)
            c = input("if want to stop print any thing or press ENTER, if no print yes: ")
            if c == "yes":
                continue
            else:
                break
        elif o == "/":
            print(n1 / n2)
            c = input("if want to stop print any thing or press ENTER, if no print yes: ")
            if c == "yes":
                continue
            else:
                break
        else:
            print("Enter real operasion \n . \n . \n . ")
