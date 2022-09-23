from typing import Optional

from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI


class Greeting(Document):
    message: str


async def init():
    client = AsyncIOMotorClient("mongodb://admin-user:admin-password@192.168.6.77:27017")
    await init_beanie(database=client.backend, document_models=[Greeting])


app = FastAPI(on_startup=[init])


@app.post("/")
async def create(name: str = "world"):
    message = Greeting(message=f"Hello {name}!")
    await message.save()
    return message

@app.get("/all")
async def get_all():
    greetings = await Greeting.find().to_list()
    return greetings

