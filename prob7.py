n1=int(input("Total number of elements you want: "))
l=[]
for i in range(0,n1,1):
    el=int(input("enter number: "))
    l.append(el)
print(l)

n2=int(input("How much element ypu want in list2: "))
l2=[]
for i in range(0,n2,1):
    ele=int(input("Enter number: "))
    l2.append(ele)
print(l2)

print(l+l2)
print(sorted(l+l2))