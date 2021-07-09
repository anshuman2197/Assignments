l=[]
while True:
    c=int(input("""
    1 Push
    2 Pop
    3 Peek
    4 Display
    5 Exist
    
    """))

    if c==1:
        n=input("Enter The Value: ")
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            (l)

    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print('Last Stack Value',l[-1])

    elif c==4:
        print('Display Stack')

    elif c==5:
        break;

    else:
        print("Invalid Choice")