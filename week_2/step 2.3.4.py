# Во входном файле заданы два целых положительных числа a и b, не превосходящие 10^18.
# Если их наименьшее общее кратное  не превосходит 10^18, выведите его значение. В противном случае выведите -1.

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return x // gcd(x, y) * y


MAX_NUMBER = 10**18
x, y = map(int, input().split())
result = lcm(x, y)
print(-1 if result > MAX_NUMBER else result)
