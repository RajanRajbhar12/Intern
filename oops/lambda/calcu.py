while True:
    print("\n1:add")
    print("2:sub")
    print("3:div")
    print("4:mul")
    print("5:exit")
    choice=input("enter a choice")

    num1=float(input("enter 1 number"))
    num2=float(input("enter 2 number"))

    

    if choice=="5":
        print("exit")
        break

    elif choice=="1":
        print("add",num1+num2)

    