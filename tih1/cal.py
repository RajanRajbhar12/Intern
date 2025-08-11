from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

class Cal(BaseModel):
    num1:float
    num2:float

@app.post("/add")
def add(number:Cal):
    result=number.num1+number.num2
    return{"result":result}

@app.post("/sub")
def sub(number:Cal):
    result=number.num1-number.num2
    return{"result":result}

@app.post("/div")
def div(number:Cal):
    result=number.num1/number.num2
    return{"result":result}
    
@app.post("/mul")
def mul(number:Cal):
    result=number.num1*number.num2
    return{"result":result}
