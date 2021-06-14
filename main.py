class book:
    def __init__(self):
        self.title=input("enter Book title:")
        self.author=input("enter Author:")
        self.publisher=input("enter publisher:")
        self.price=int(input("enter Price:"))

    def setter(self):
        self.title=input("enter Book title:")
        self.author=input("enter Author:")
        self.publisher=input("enter publisher:")
        self.price=int(input("enter Price:"))
        return

    def getter(self):
        print("Book title: {} \n Book author: {}\n Book publisher: {}\n Book price: {}".format(self.title,self.author,self.publisher,self.pice))
        return

    def royalty(self,sale):
        if(sale<=500):
            self.royalty=self.price*0.10
            return self.royalty
        elif(sale<=1000):
            self.royalty=self.price*0.125
            return self.royalty
        else:
            self.royalty=self.price*0.15
            return self.royalty
        
class ebook(book):
    def __init__(self):
        super().__init__()
        self.format=input("Add ebook format (EPUB, PDF, MOBI etc)")

    def royalty(self, sale):
        if(sale<=500):
            self.royalty=(self.price-self.price*0.12)*0.10
            return self.royalty
        elif(sale<=1000):
            self.royalty=(self.price-self.price*0.12)*0.125
            return self.royalty
        else:
            self.royalty=(self.price-self.price*0.12)*0.15
            return self.royalty

b1=book()
sale=int(input("Enter total sale of book.."))
print("royalty amount on book is:",b1.royalty(sale))

eb1=ebook()
sale=int(input("Enter total sale of book.."))
print("royalty amount of book is:",eb1.royalty(sale))