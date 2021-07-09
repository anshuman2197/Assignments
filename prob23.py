class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def greet(self):
        print("Welcome",self.name)

e1=Employee("Pardeep",123444)
print(e1.name)
print(e1.id)
e1.greet()

e2=Employee("Naveen",24657)
print(e2.name)
print(e2.id)
e2.greet()