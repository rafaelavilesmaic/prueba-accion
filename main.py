from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hola Mundo desde FastAPI! cambio",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
