import asyncio
from enum import Enum

class PrimalityStrategy(str, Enum):
    full = "full"
    half = "half"
    sqrt = "sqrt"

STRATEGIES = {
    PrimalityStrategy.full: lambda num: num,
    PrimalityStrategy.half: lambda num: num // 2 + 1,
    PrimalityStrategy.sqrt: lambda num: num ** 0.5 + 1,
}

async def calculate_primes_for_generator(target_number):
    for num in range(0, target_number + 1):
        if num < 2:
            continue

        is_prime = is_prime_num(num)
        if is_prime:
            await asyncio.sleep(0.2)
            yield num

def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True