# У вас есть n слитков золота, каждый имеет свой вес. Также у вас есть рюкзак вместимости S.
# Необходимо вычислить максимальный вес, который вы можете с собой унести. Вы можете дробить слитки.

s, n = map(int, input().split())
arr = [int(i) for i in input().split()]
print(min(s, sum(arr)))
