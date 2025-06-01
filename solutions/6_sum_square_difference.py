def square_sum(n: int) -> int:
    return sum(range(n+1)) ** 2

def sum_square(n: int) -> int:
    res = 0

    for i in range(n+1):
        res += i**2

    return res

def sum_square_difference(n: int) -> int:
    s_sq = sum_square(n)
    sq_s = square_sum(n)

    return sq_s - s_sq


ans = sum_square_difference(100)
print(ans)