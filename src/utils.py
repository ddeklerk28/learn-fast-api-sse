import asyncio
from math import ceil
from enum import Enum

class PrimalityStrategy(str, Enum):
    full = "full"
    half = "half"
    sqrt = "sqrt"

STRATEGIES = {
    PrimalityStrategy.full: lambda num: num,
    PrimalityStrategy.half: lambda num: num // 2 + 1,
    PrimalityStrategy.sqrt: lambda num: ceil(num ** 0.5) + 1,
}

async def calculate_primes_generator(target_number, strategy: PrimalityStrategy):
    get_factor_upper_limit = STRATEGIES[strategy]
    for num in range(0, target_number + 1):
        if num < 2:
            continue

        is_prime = is_prime_num(get_factor_upper_limit(num))
        if is_prime:
            await asyncio.sleep(0)
            yield num

def is_prime_num(factor_upper_limit):
    for i in range(2, factor_upper_limit):
        if factor_upper_limit % i == 0:
            return False
    return True