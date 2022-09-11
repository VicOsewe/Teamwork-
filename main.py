
from fastapi import FastAPI

app = FastAPI(title="TeamWork", version="1.0.0")


@app.get("/")
def hello_api():
    return {"msg": "Hello API"}
