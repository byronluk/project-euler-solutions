from collections import defaultdict


# find the prime factors of a number
def factors(num):
    res = defaultdict(int)

    for i in range(2, num + 1):
        if i == 0:
            return res

        while num != 0 and num % i == 0:
            num = num / i
            res[i] += 1

    return res


def smallest_multiple(n: int) -> int:
    result = 1
    highest_powers = defaultdict(int)

    # find the highest power of each prime factor in the range 1 to n
    for i in range(1, n + 1):
        powers = factors(i)
        for k, v in powers.items():
            highest_powers[k] = max(highest_powers[k], v)

    # multiply the highest powers of each prime factor together
    for k, v in highest_powers.items():
        result *= k**v

    return result


print(smallest_multiple(20))  # 232792560
