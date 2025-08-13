import time

def deco(func):
    def wrap(*args,**kwargs):
        start=time.time
        result=func(*args,**kwargs)
        end=time.time
      
        return result
    return wrap

@deco
def yoo():
    time.sleep(2)
    print("done")

def hii():
    time.sleep(3)
    print("ok")

yoo()
hii()
