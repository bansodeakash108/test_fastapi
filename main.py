from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"ms....g": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}