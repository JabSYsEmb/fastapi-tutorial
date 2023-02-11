from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "frontend:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{name}")
async def root(name) :
    return {"message": "Hello - {}!".format(name)}

@app.get("/items/{items}")
async def root(items: int) :
    return {"message": "Hello - {}!".format(items)}

@app.get("/person/api")
async def person():
    return {"employee_number" : "2", "accountant": "Mustafa Faruk"}

@app.get("/person")
async def person():
    return {"employee": "Ahmed Murat", "salary": 2000, "position": "DevOps"}

