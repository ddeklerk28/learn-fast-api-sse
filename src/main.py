from fastapi import FastAPI, Request
from fastapi.sse import EventSourceResponse, ServerSentEvent
from fastapi.staticfiles import StaticFiles

from .utils import calculate_primes_generator, PrimalityStrategy

app = FastAPI()

app.mount("/ui", StaticFiles(directory="src/static", html=True), name="ui")

@app.get("/")
async def home():
    return "Welcome home!"

@app.get("/items/stream", response_class=EventSourceResponse)
async def sse_items(request: Request, limit: int = 1000, strategy: PrimalityStrategy = PrimalityStrategy.full):
    async for num in calculate_primes_generator(limit, strategy):
        if await request.is_disconnected():
            break
        yield ServerSentEvent(data=num, event="prime_number", id=str(num))