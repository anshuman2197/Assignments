# class Mobile:
#     def __init__(self):
#         print("Mobile Constructor Called")

# realme=Mobile()

class Mobile:
    def __init__(self):
        self.model="Realme X"

    def show_model(self):
        print(self.model)

realme=Mobile()
redmi=Mobile()
oneplus=Mobile()
print(realme.model)
print(redmi.model)
print(oneplus.model)
print()
redmi.model="Redmi 9pro"
print(realme.model)
print(redmi.model)
print(oneplus.model)
