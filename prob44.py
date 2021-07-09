class Bank_Account:
   def __init__(self):
         self.balance=0
         print("Welcome to Check Your Balance Account")

   def deposit(self):
         x=input("Enter amont to deposite: ")
         amount=float(x)
         self.balance+=amount
         print("You Deposite An Amount of", amount)

   def withdraw(self):
         x=input("Enter amount to be Withdraw: ")
         amount=float(x)
         if self.balance>=amount:
             self.balance-=amount
             print("You Withdraw: ",amount)
         else:
             print("Net Available Balance of Your Account is: ",self.balance)
   
   def display(self):
         print("Your Net Available Balance is: ",self.balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
