# Как-то профессор Налейпиво заметил, что один из студентов на его лекции уделяет слишком много внимания мобильному
# телефону. Подкравшись сзади (а несмотря на большие размеры, профессор Налейпиво умеет незаметно подкрадываться),
# профессор обнаружил смягчающее вину студента обстоятельство - тот не отправлял SMS-ки, а увлечённо играл в
# следующую игру. Есть поле размером N×M ячеек и несколько (возможно ноль) стен между ячейками. Одна из ячеек
# является стоком, в то время как одна из оставшихся занята уткой. Ваша задача привести утку в сток. Единственный
# способ передвижения утки, доступный вам - это скольжение, что подразумевает, что вы можете толкнуть утку в одном
# из четырёх направлений, и она будет скользить в нем, пока не упрется в стену. Вы не можете толкнуть утку снова,
# пока она не остановится. Уровень считается пройденным, если утка останавливается в стоке. Если утка просто
# проскользнула через сток, не остановившись, уровень не считается пройденным.
#
# Профессор остановил лекцию и попросил студента создать несколько своих уровней. Он расчертил на доске уровень,
# нанёс стены, поместил сток, и теперь студенту надо разместить где-то утку. Профессор выбрал несколько мест,
# куда бы он хотел поместить её, и предложил студенту описать алгоритм прохождения уровня. Студент быстро понял,
# что это ловушка - среди них есть такие, начав игру из которых, довести утку до стока невозможно. А сумеете ли это
# сделать Вы? Ваша задача - имея размеры поля, позицию стен и стока, а также выбранные позиции для утки, найти среди
# выбранных позиций такие, начав игру из которых пройти уровень возможно.


from collections import deque


class Solution:
    def __init__(self):
        self.board = []
        self.s = ()
        self.distances = []
        self.n = 0
        self.m = 0

    def read_data(self):
        self.n, self.m = map(int, input().split())
        #  input()
        self.distances = [[False] * self.m for _ in range(self.n)]
        self.board = [[' ' for _ in range(2 * self.m + 1)] for _ in range(2 * self.n + 1)]
        for i in range(2 * self.n + 1):
            s = input()
            for j in range(2 * self.m + 1):
                self.board[i][j] = s[j]
                if s[j] == 'S':
                    self.s = (i, j)
                elif s[j] == 'D':
                    self.board[i][j] = 'D'

    def check(self, pair_x, pair_y):
        if 0 <= pair_x < len(self.board) and 0 <= pair_y < len(self.board[0]) and \
                self.board[pair_x][pair_y] != '-' and self.board[pair_x][pair_y] != '|':
            return True
        return False

    def is_wall(self, x, y):
        return self.board[x][y] != '-' and self.board[x][y] != '|'

    def set_distance(self, pair_x, pair_y, value=False):
        self.distances[(pair_x - 1) // 2][(pair_y - 1) // 2] = value

    def get_distance(self, pair_x, pair_y):
        return self.distances[(pair_x - 1) // 2][(pair_y - 1) // 2]

    def bfs(self):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        q.append(self.s)

        self.set_distance(self.s[0], self.s[1])

        while q:
            currentCell = q.popleft()
            for dir in dirs:
                if self.is_wall(currentCell[0] + dir[0], currentCell[1] + dir[1]):
                    continue
                tmpCell_x = currentCell[0]
                tmpCell_y = currentCell[1]

                while self.check(tmpCell_x, tmpCell_y):
                    if self.board[tmpCell_x][tmpCell_y] == 'D':
                        self.board[tmpCell_x][tmpCell_y] = 'E'

                    if not self.get_distance(tmpCell_x, tmpCell_y):
                        if (tmpCell_x * tmpCell_y - 1) % 2 == 0:
                            q.append((tmpCell_x, tmpCell_y))
                            self.set_distance(tmpCell_x, tmpCell_y, True)

                    tmpCell_x -= dir[0]
                    tmpCell_y -= dir[1]

                tmpCell_x += dir[0]
                tmpCell_y += dir[1]

                if not self.get_distance(tmpCell_x, tmpCell_y):
                    if (tmpCell_x * tmpCell_y - 1) % 2 == 0:
                        q.append((tmpCell_x, tmpCell_y))
                        self.set_distance(tmpCell_x, tmpCell_y, True)

                    if self.board[tmpCell_x][tmpCell_y] == 'D':
                        self.board[tmpCell_x][tmpCell_y] = 'E'

    def print_board(self):
        for row in self.board:
            for el in row:
                if el == 'D':
                    print(' ', end='')
                elif el == 'E':
                    print('D', end='')
                else:
                    print(el, end='')
            print()


solution = Solution()
solution.read_data()
solution.bfs()
solution.print_board()
