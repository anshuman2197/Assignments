# python program to check if a given key exits or not


d={"Rahul":"Developer","Tina":'SEO',"Sam":"Trainer","Madhu":"Developer","Rahul":"digital Marketting"}
user=input("Enter key you want: ")
if user in d:
    print("the key is present")
    print("The value is", d[user])
else:
    print("the key is absent")
