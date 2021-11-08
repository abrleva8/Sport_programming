# По заданным целым a, b и c (0 < |a|,|b|,|c| <= 10**6 )
# вычислите, имеет ли уравнение a*x + b*y = c хотя бы одно целочисленное решение.
# Если у уравнения есть решение, выведите 1, если нет  выведите 0.

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


a, b, c = map(int, input().split())
g = gcd(a, b)
print(int(c % g == 0))
