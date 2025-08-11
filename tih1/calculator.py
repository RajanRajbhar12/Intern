from pydantic import BaseModel

class Cal(BaseModel):
    num1:float
    num2:float

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    if num2==0:
        return " divided by 0 is not allowed"
    return num1/num2

def mul(num1,num2):
    return num1*num2        