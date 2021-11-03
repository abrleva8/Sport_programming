# Даны два целых положительных числа a > b, не превосходящие 10^9.
# Сколько раз в алгоритме Евклида при вычислении их НОД будет использована операция взятия остатка?


def gcd(x, y):
    global i
    if y == 0:
        return x
    else:
        i += 1
        return gcd(y, x % y)


i = 0
x, y = map(int, input().split())

gcd(x, y)

print(i)
