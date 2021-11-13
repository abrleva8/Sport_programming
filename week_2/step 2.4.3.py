# Даны три целых числа a, n и m (1≤a≤10^9, 2≤n≤10^6,2≤m≤10^9
# Найти значение выражения 1/a+2/a^2+3/a^3+ ... + n/a^n по модулю m. Если какое-то из делений невозможно, выведите -1.

def m_mul(x, y, mod):
    return ((x % mod) * (y % mod)) % mod


def extended_gcd(a, b):
    if not b:
        return 1, 0, a
    y, x, g = extended_gcd(b, a % b)
    return x, y - (a // b) * x, g


def div_2(a, b, mod):
    x, y, gcd = extended_gcd(b, mod)
    if a % gcd != 0:
        return -1
    return m_mul(a // gcd, x, mod)


def find_answer(a, n, m):
    a %= m
    tmp_a = div_2(1, a, m)
    if tmp_a == -1:
        return -1
    tmp_b, tmp_sum = tmp_a, 0

    for i in range(1, n + 1):
        tmp_div = m_mul(i, tmp_b, m)
        tmp_sum = (tmp_sum + tmp_div) % m
        tmp_b = (tmp_a * tmp_b) % m
    return tmp_sum

a, n, m = map(int, input().split())
result = find_answer(a, n, m)
print(result)
