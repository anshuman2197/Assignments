n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
opr=input("Enter the operator:  ")
if opr=="+":
    print(n1+n2)
elif opr=="-":
    print(n1-n2)
elif opr=="*":
    print(n1*n2)
elif opr=="/":
    print(n1/n2)
elif opr=="%":
    print(n1%n2)
else:
    print("Invalid Operation")