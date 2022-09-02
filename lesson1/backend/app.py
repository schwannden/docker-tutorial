from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = "world"):
    return {"message": f"Hello {name}!"}

