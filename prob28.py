class Student:
    def check(self):
        if self.marks>=40:
            return True
        else:
            return False

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

student1=Student("Harry",85)
student2=Student("Snam",40)
pass_fail=student1.check()
print(pass_fail)
pass_fail=student2.check()
print(pass_fail)
