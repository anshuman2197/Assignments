# class Myclass():
#     def show(self):
#         print("I am a Method")

# x=Myclass()
# x.show()

class Mobile:
    def __init__(self,m):
        self.model=m
    
    def show_model(self,p):
        self.price=p
        print("Model",self.model,"Price:",self.price)

realme=Mobile('Realme X')
realme.show_model(1000)
print(id(realme))

redmi=Mobile('Redmi 9pro')
redmi.show_model('12000')
print(id(redmi))