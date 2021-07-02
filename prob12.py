n=int(input('Enter total number of key value pair you want: '))
d={}
for i in range(n):
    k=input('Enter the key: ')
    v=input('Enter the value: ')
    d.update({k:v})

print(d)