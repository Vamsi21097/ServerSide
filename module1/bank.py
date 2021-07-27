class Bank:
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner
        print ("The account is created")
        
    def deposit(self):
        amount = float(input("Enter the amount to be deposit: "))
        self.balance = self.balance + amount
        print ("Deposit is successful and the balance in the account is %f" % self.balance)
    
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print ("The withdraw is successfull and balance is %f" % self.balance)
        else:
            print ('Insuficient Balance')
    
    def enquiry(self):
        print ("Balance in the acount is %f" % self.balance)
        
balance=0
owner="jyothi"
acc = Bank(balance,owner)
acc.deposit()
acc.withdraw()
acc.enquiry()