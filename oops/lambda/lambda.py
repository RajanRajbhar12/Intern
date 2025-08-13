s1="geeksforgeeks"

s2=lambda fun:fun.upper()

print(s2(s1))

n=lambda x :"positive" if x > 5 else "negative" if x > 0 else"zero"

print(n(5))
print(n(-2))
print(n(6))

def add(x):
    return x **2 

print(add(2))

re = lambda x : x**2
print(re(5))

raj=lambda x: "yes"if x/2 else "no"
print(raj(20))

hii=[lambda arg=x: arg*2 for x in range(1,5)]
for i in hii:
    print(i())

cal=lambda x,y:(x+y,x*y,x/y)
res=cal(4,6)
print(res)

la=lambda x: x*2
print(la(5))