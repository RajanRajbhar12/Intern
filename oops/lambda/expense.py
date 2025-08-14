expense=[]


while True:
    description=input("enter the details:")
    amount=float(input("enter the amount:"))
    expense.append((description,amount))
    print(f"{expense}")
    print(f" Expense: {description}:{amount}")


    a=input("u want to continue press 1 or 2 to exit:")
    if a=="1":
        print("continue")
    elif a=="2":
        break
    
