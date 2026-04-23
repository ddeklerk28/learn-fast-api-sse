def calculate_primes_for(target_number):
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