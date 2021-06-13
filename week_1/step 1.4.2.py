# Дана окружность, многочлен и точка X.
# Гарантируется, что (x, f(x))(x,f(x)) лежит внутри окружности.
# Найти пересечение многочлена с окружностью.


# return f(x), where f is polynom with @coefficients
def f(coefficients, x):
    result = 0
    temp = 1
    degree = len(coefficients)
    for i in reversed(range(degree)):
        result += coefficients[i] * temp
        temp *= x
    return result


# return distance between the points: (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return result


# return axis X of the intersection point of the polynom and circle
def intersection_point(c_x, c_y, c_d, a, x):
    eps = 1e-09
    left = x
    right = x + c_d
    while abs(distance((right + left) / 2, f(a, (right + left) / 2), c_x, c_y) - c_d) > eps:
        mid = (right + left) / 2
        if distance(mid, f(a, mid), c_x, c_y) > c_d:
            right = mid
        else:
            left = mid
    result = (right + left) / 2
    return result


c_x, c_y, c_d = map(int, input().split())
n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

result = intersection_point(c_x, c_y, c_d, a, x)
print(result)
