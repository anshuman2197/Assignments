# python to concate two dict

n=int(input("Enter total: "))
d1={}
for i in range(n):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d1.update({k:v})

print(d1)

n2=int(input("Enter total n2: "))
d2={}
for i in range(n2):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d2.update({k:v})

print(d2)

d1.update(d2)
print("concatenation",d1)