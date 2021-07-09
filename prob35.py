# user=input('Enter a value')
# # print(list(user))
# l=user.split()
# print(l)

x=int(input("Enter the value"))
l=[]
# for i in range(x):
#     n=input("Enter the value: ")
#     l.append(n)
# print(l)

for i in range(x):
    n=input("Enter the value: ").split()
    l.append(n)
print(l)