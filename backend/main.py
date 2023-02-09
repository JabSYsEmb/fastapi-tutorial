from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
async def root(name) :
    return {"message": "Hello {}!".format(name)}

@app.get("/items/{items}")
async def root(items: int) :
    return {"message": "Hello {}!".format(items)}

@app.get("/person/api")
async def person():
    return {"employee_number" : "3", "accountant": "Mustafa Faruk"}

@app.get("/person")
async def person():
    return {"employee": "Ahmed Murat", "salary": 2000, "position": "DevOps"}

