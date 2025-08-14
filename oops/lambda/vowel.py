def count(s):
    vowels=["a","o","e"]
    count=0
    for char in s.lower():
        if char in vowels:
            count +=1
    return count
    
print(count("hello"))

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

fizzbuzz(20)