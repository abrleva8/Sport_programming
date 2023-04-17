# Дан ориентированный ацикличный граф G. Проверить, что существует единственный топологический порядок вершин графа.

def dfs(u):
    stack = [u]
    while stack:
        v = stack[-1]
        free.discard(v)
        p = graph[v] & free
        if p:
            stack.append(p.pop())
        else:
            order.append(stack.pop())


n, m = map(int, input().split())
graph = tuple(set() for _ in range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)

free = set(range(1, n + 1))
order = []

while free:
    dfs(free.pop())

print(['NO', 'YES'][all(x in graph[y] for x, y in zip(order[-2::-1], order[::-1]))])
