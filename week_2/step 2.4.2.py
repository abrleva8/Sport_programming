# Заданы четыре целых числа a, b, c, d (1≤∣a∣,∣b∣,∣c∣,∣d∣≤10^9). Вычислите (ad+bc)/(bd) mod (10^9+7).

def norm(d, mod):
    return ((d % mod) + mod) % mod


def fast_pow(a, n, mod):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * fast_pow(a, n - 1, mod) % mod
    else:
        tmp = fast_pow(a, n//2, mod)
        return (tmp * tmp) % mod


def m_mul(x, y, mod):
    return norm(norm(x, mod) * norm(y, mod), mod)


# @pmod is a prime number
def m_div(a, b, pmod):
    return m_mul(a, fast_pow(b, pmod - 2, pmod), pmod)

a, b, c, d = map(int, input().split())
p = 10**9 + 7
first_sum = m_div(a, b, p)
second_sum = m_div(c, d, p)
result = (first_sum + second_sum) % p
print(result)
