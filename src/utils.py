import asyncio

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