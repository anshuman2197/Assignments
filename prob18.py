# check a number is spy or not

n=int(input("Enter a number: "))
sum=0
p=1
while n>0:
    rem=n%10
    sum+=rem
    p*=rem
    n//=n

if sum==p:
    print("It is a Spy number")
else:
    print("It is not a spy number")