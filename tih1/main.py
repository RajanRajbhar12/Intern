from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

from calculator import Cal,add,sub,div,mul

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient("mongodb://localhost:27017/")
db = client["thirdtask"]
users_collection = db["users"]

class User(BaseModel):
    email: str
    password: str

@app.post("/signup")
async def signup(user: User):
    users_collection.insert_one(user.model_dump())
    return {"message": "User saved!"}

@app.post("/login")
async def login(user: User):
    found = users_collection.find_one({"email": user.email, "password": user.password})
    if found:
        return {"success": True}
    else:
        return {"success": False}
    
@app.post("/calc/add")
def calc_add(numbers: Cal):
    return {"result": add(numbers.num1, numbers.num2)}

@app.post("/calc/sub")
def calc_sub(numbers: Cal):
    return {"result": sub(numbers.num1, numbers.num2)}

@app.post("/calc/mul")
def calc_sub(numbers: Cal):
    return {"result": mul(numbers.num1, numbers.num2)}

@app.post("/calc/div")
def calc_sub(numbers: Cal):
    return {"result": div(numbers.num1, numbers.num2)}

@app.post("/")
async def root():
    return {"message": "API is working!"}

