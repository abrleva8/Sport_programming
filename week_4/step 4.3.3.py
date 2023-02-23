# (p,q)-лошадь - это обобщение обычного шахматного коня. (p,q)-лошадь своим ходом перемещается на p клеток в одном
# направлении, и на q - в другом (перпендикулярном). Например, (3,4)-лошадь может переместиться с клетки (5,6) на
# клетки (1,3), (2,2), (2,10), (1,9), (8,10), (9,9), (8,2) и (9,3). Очевидно, что обычный шахматный конь -
# это (2,1) - лошадь. Ваша задача - определить минимальное число ходов, которое требуется (p,q)-лошади, чтобы добраться
# от одной клетки шахматной доски M×N до другой. За пределы доски выходить запрещается.

import queue


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PQKnight:

    def __init__(self):
        self.end = None
        self.start = None
        self.q = None
        self.p = None
        self.distances = None

    def read_data(self):
        data = list(map(int, input().split()))
        m, n = data[0], data[1]
        self.p, self.q = data[2], data[3]
        self.distances = [[-1 for _ in range(n)] for _ in range(m)]
        self.start = Pair(data[4] - 1, data[5] - 1)
        self.end = Pair(data[6] - 1, data[7] - 1)

    def check(self, pair):
        return 0 <= pair.x < len(self.distances) and 0 <= pair.y < len(self.distances[0])

    def bfs(self):
        dx = [-self.q, -self.p, self.p, self.q, self.q, self.p, -self.p, -self.q]
        dy = [self.p, self.q, self.q, self.p, -self.p, -self.q, -self.q, -self.p]

        q = queue.Queue()
        q.put(self.start)
        self.distances[self.start.x][self.start.y] = 0
        while not q.empty():
            current_cell = q.get()
            for i in range(len(dx)):
                next_cell = Pair(current_cell.x + dx[i], current_cell.y + dy[i])

                if not self.check(next_cell):
                    continue

                if self.distances[next_cell.x][next_cell.y] == -1:
                    q.put(next_cell)
                    self.distances[next_cell.x][next_cell.y] = self.distances[current_cell.x][current_cell.y] + 1

    def print_result(self):
        print(self.distances[self.end.x][self.end.y])


if __name__ == '__main__':
    pq_knight = PQKnight()
    pq_knight.read_data()
    pq_knight.bfs()
    pq_knight.print_result()
