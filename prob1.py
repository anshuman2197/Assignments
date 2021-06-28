n1=int(input("Enter number of Hindi: "))
n2=int(input("Enter number of English: "))
n3=int(input("Enter number of Maths: "))
n4=(n1+n2+n3)/3
if n4>=90:
    print("Grade A")
elif n4>=80 and n4<90:
    print("Grade B")
elif n4>=70 and n4<80:
    print("Grade C")
elif n4>=60 and n4<70:
    print("Grade D")
else:
    print("Grade F")

