n=int(input("Enter Number: "))
flag=0
for i in range(1,n):
    if i*i==n:
        flag=1
        break

if flag==1:
    print("Perfect square")

else:
    print("not perfect square")