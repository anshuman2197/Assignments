# Sum of all the values in dictionary

n=int(input("Enter total num,ber of pair: "))
d={}
for i in range(n):
    k=input("Enter the Key: ")
    v=int(input('Enter the Value: '))
    d.update({k:v})
print(d)

print(sum(d.values()))