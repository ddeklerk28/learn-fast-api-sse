from collections.abc import AsyncIterable

import asyncio
from fastapi import FastAPI
from fastapi.sse import EventSourceResponse
from pydantic import BaseModel
from starlette.responses import StreamingResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None

items = [
    Item(name="Plumbus", description="A multi-purpose household device."),
    Item(name="Portal Gun", description="A portal opening device."),
    Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
]

async def calculate_primes_for(target_number):
    for num in range(0, target_number + 1):
        if num < 2:
            continue

        is_prime = test_for_prime(num)
        if is_prime:
            yield f"data: {num}"

def test_for_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

@app.get("/")
async def home():
    return "Welcome home!"

@app.get("/items/stream", response_class=EventSourceResponse)
async def sse_items():
    return StreamingResponse(calculate_primes_for(1000), media_type="text/event-stream")