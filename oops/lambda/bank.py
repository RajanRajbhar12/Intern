class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.history=[]

    def deposit(self,amount):
        self.balance +=amount
        self.history.append(f"deposited {amount}")
        print(f"deposited {amount}.new balance{self.balance}")

    def withdraw(self,amount):
        self.balance -=amount
        self.history.append(f"withdraw{amount}")
        print(f"withdraw {amount}.new balance{self.balance}")

    def history(self):
        if not self.history:
            print("no transaction")
        else:
            print("transaction")
            for transaction in self.history:
                print(transaction)

account=Bank("rajan")

while True:
    print("\n1:deposit")
    print("2:withdraw")
    print("3:history")

    choice=input("enter a choice")

    if choice=="1":
        amount=float(input("enter a amount"))
        account.deposit(amount)
    
    elif choice=="2":
        amount=float(input("enter a amount"))
        account.withdraw(amount)