class Student:
    def check(self):
        if self.marks>=40:
            return True
        else:
            return False

student1=Student()
student1.name="Harry"
student1.marks=85

print(student1.name)
print(student1.marks)

pass_fail=student1.check()
print(pass_fail)

student2=Student()
student2.name="Zennith"
student2.marks=30

pass_fail=student2.check()
print(pass_fail)