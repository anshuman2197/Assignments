class Mobile:
    fp="Yes"

    def __init__(self):
        self.model="realme X"

    def show(self):
        print("Model: ",self.model)

    @classmethod
    def f(cls):
        print("Finger: ",cls.fp)
    
realme=Mobile()
realme.show()
Mobile.f()