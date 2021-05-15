# Два максимума.
#
# Дан массив. Вам требуется определить позиции первого максимума и второго максимума.

n = int(input())
cur, a, b = map(int, input().split())
mod = 1791791791

def next_rand():
    global cur
    cur = (cur * a + b) % mod
    return cur

a = [next_rand() for i in range(n)]

first_max = -1
#second_max = -1
pos_first_max = -1
#pos_second_max = -1

for i in range(n):
    if a[i] > first_max:
        pos_second_max = pos_first_max
        second_max = first_max
        pos_first_max = i
        first_max = a[i]
    elif a[i] > second_max:
        pos_second_max = i
        second_max = a[i]

# print(*a)
# print(first_max)
# print(second_max)
print(pos_first_max + 1, end=" ")
print(pos_second_max + 1)
