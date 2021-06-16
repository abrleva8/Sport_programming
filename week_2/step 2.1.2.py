# Входные данные содержат одно целое число N  (2 <= N <= 10^9)
# Если число является простым, выведите 1, если число является составным, выведите 0.


# @n is int number up to 10**9
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i = i + 1
    return 1


N = int(input())
result = is_prime(N)
print(result)
