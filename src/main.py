from fastapi import FastAPI, Request
from fastapi.sse import EventSourceResponse, ServerSentEvent

from .utils import calculate_primes_for_generator

app = FastAPI()

@app.get("/")
async def home():
    return "Welcome home!"

@app.get("/items/stream", response_class=EventSourceResponse)
async def sse_items(request: Request, limit: int = 1000):
    async for num in calculate_primes_for_generator(limit):
        if await request.is_disconnected():
            break
        yield ServerSentEvent(data=num, event="prime_number", id=str(num))