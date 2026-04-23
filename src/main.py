from fastapi import FastAPI
from fastapi.sse import EventSourceResponse

from .utils import calculate_primes_for_generator

app = FastAPI()

@app.get("/")
async def home():
    return "Welcome home!"

@app.get("/items/stream", response_class=EventSourceResponse)
async def sse_items():
    async for num in calculate_primes_for_generator(1000):
        yield num