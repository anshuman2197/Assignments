l=[]
while True:
    c=int(input("""
    1 Push
    2 Pop
    3 Front
    4 Last
    5 Display
    6 Exit
    
    """))

    if c==1:
        n=input("Enter Value: ")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("Empty queue")
        else:
            del l[0]
            print(l)

    elif c==3:
        if len(l)==0:
            print("Empty queue")
        else:
            print("First queue ",l[0])

    elif c==4:
        if len(l)==0:
            print("Empty queue")
        else:
            print("Last queue ",l[-1])
    elif c==5:
        if len(l)==0:
            print("Display Queue")

    elif c==6:
        break;
    
    else:
        print("Invalid Number")