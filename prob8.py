import random

a=int(input('Enter Number: '))
l=[]
for i in range(0,a,1):
    n=random.randint(1,20)
    l.append(n)
print(l)
l.sort()
print(l)