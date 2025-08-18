expenses= []

def add(description,amount):
    expenses.append({"description":description,"amount":amount})
    print(f"added:{description} -{amount}")
    print(f"All expenses :{expenses}")

def total():
    total = sum(item["amount"] for item in expenses)
    return total

add("Lunch",50)
add("snacks",30)
print("Total",total())