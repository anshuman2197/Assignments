n1=float(input('Enter First number: '))
n2=float(input("Enter second Number: "))
opr=input("+,/,-,* Enter any one operator: ")
if opr=="+":
    print("Addition: ",n1+n2)
elif opr=="-":
    print("Subtraction: ",n1-n2)
elif opr=="*":
    print("Multiplication: ",n1*n2)
elif opr=="/":
    print("Division: ",n1/n2)
else:
    print("Invalid operator")