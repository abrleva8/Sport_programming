# Путь КузнечиКа
#
# Перед клетчатой полоской длины nn сидит кузнечиК. В каждой клетке написано какое-то число.
# КузнечиК умеет прыгать на 1, 2, \ldots k1,2,…k клеток вперед.
# Необходимо попасть в самую правую клетку, набрав при этом минимально возможную сумму.

from collections import deque
n, k = map(int, input().split())
zero = (0, 0, None)
deq, r = deque((zero,)), []
for i, w in enumerate(map(int, input().split()), 1 - k):
    seed = deq[0]
    if seed[1] < i:
        del deq[0]
        seed = deq[0]
    w += seed[0]
    while deq and deq[-1][0] >= w:
        del deq[-1]
    deq.append((w, i + k, seed))
seed = deq.pop()
while seed is not zero:
    _, x, seed = seed
    r.append(x)
print(w, len(r))
print(' '.join(map(str, r[::-1])))
