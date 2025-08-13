from fastapi import FastAPI

app=FastAPI()

def logging(func):
    def wrapper(*args,**kwargs):
        print(f"calling function :{func.__name__}")
        return func(*args,**kwargs)
    return wrapper

tasks=[]
@logging
@app.post("/add/")
def add_task(task:str):
    tasks.append(task)
    return{"message":"task added succefully","task": task }
@logging
@app.get("/get/")
def get_task():
    return{"tasks":tasks}