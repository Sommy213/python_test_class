class BankAccount:
    def __init__(self,accnum,acctnamme,balance =0):
    
        self.history =[]
        self.acctname = acctnamme
        self.amountnum = accnum
      
        self.balance = balance
        
        print("hello  welcome to opay")
    def deposit(self,amt):
        self.balance += amt
       
        self.history.append(f"you just dissipted the amount{amt}")
        print(f"amt in the account: {amt}")
    def withdraw (self,amt):
      
    
        if self.balance < amt:
            print ("insuffuint fund")
        else:
            self.balance-=amt
            print(f"the amount is{amt}")
            
    def display(self):
        print("\n Amount of the balance ", self.balance)

john= BankAccount("john",123435)
john.deposit( 50000)
john.balance(0)