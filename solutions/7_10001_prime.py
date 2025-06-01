import math

def approx_nth_prime(n: int) -> int:
    return round(n * math.log(n * math.log(n)))

def compute_nth_prime(n: int) -> int:
    approx = approx_nth_prime(n)
    sieve = [False] * (approx+1)
    primes = []

    for i in range(2, approx+1):
        if sieve[i]:
            continue

        primes.append(i)
        for j in range(i*2, len(sieve), i):
            sieve[j] = True

    return primes[n-1]

print(compute_nth_prime(10001))
