# class BankAccount:
#     def __init__(self,accnum,acctnamme,balance =0):
    
#         self.history =[]
#         self.acctname = acctnamme
#         self.amountnum = accnum
      
#         self.balance = balance
        
#         print("hello  welcome to opay")
#     def deposit(self,amt):
#         self.balance += amt
       
#         self.history.append(f"you just dissipted the amount{amt}")
#         print(f"amt in the account: {amt}")
#     def withdraw (self,amt):
      
    
#         if self.balance < amt:
#             print ("insuffuint fund")
#         else:
#             self.balance-=amt
#             print(f"the amount is{amt}")
            
#     def display(self):
#         print("\n Amount of the balance ", self.balance)

# john= BankAccount("john",123435)
# john.deposit( 50000)
# john.balance(0)
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"${amount} withdrawn. New balance: ${self.balance}"
        else:
            return "Invalid or insufficient funds."

    def get_balance(self):
        return f"Balance: ${self.balance}"
def main():
    accounts = {}
    while True:
        print("\nBank Account System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                accounts[account_number] = Account(account_number)
                print(f"Account {account_number} created!")

        elif choice == 2:
            account_number = input("Enter account number: ")
            if account_number not in accounts:
                print("Account not found.")
            else:
                amount = float(input("Enter amount to deposit: "))
                print(accounts[account_number].deposit(amount))

        elif choice == 3:
            account_number = input("Enter account number: ")
            if account_number not in accounts:
                print("Account not found.")
            else:
                amount = float(input("Enter amount to withdraw: "))
                print(accounts[account_number].withdraw(amount))

        elif choice == 4:
            account_number = input("Enter account number: ")
            if account_number not in accounts:
                print("Account not found.")
            else:
                print(accounts[account_number].get_balance())

        elif choice == 5:
            print("Thank you for using the bank system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
