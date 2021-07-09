class Triangle:
    def __init__(self,sides):
        self.sides=sides

    def side(self):
        perimeter=sum(self.sides)
        return perimeter


n1=Triangle([8,9,10])
print(n1.side())