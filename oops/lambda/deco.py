def deco(func):
    def wrap():
        print("before")
        func()
        print("after")
    return wrap

@deco
def hel():
    print("hello world")

hel()

def fun(f,x):
    return f(x)

def square(x):
    return x*x

res =fun(square,5)
print(res)
print(square(5))

