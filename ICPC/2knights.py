from collections import deque

def find_min_moves(board_size, start1, start2):
    queue = deque([(start1, start2, 0)])  # Очередь с начальными координатами и числом шагов
    visited = set([(start1, start2)])  # Множество посещенных клеток

    # Возможные варианты ходов коней (относительные координаты)
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    while queue:
        knight1, knight2, steps = queue.popleft()

        if knight1 == knight2:
            return steps, knight1  # Встреча произошла, возвращаем число шагов и координаты встречи

        for move in moves:
            x1 = knight1[0] + move[0]
            y1 = knight1[1] + move[1]
            x2 = knight2[0] + move[0]
            y2 = knight2[1] + move[1]

            queue.append(((x1, y1), (x2, y2), steps + 1))
            visited.add((x1, y1))

    return -1, None  # Встреча невозможна

# Пример использования
board_size = int(input("Введите размер шахматной доски: "))
start1 = tuple(map(int, input("Введите начальную позицию белого коня: ").split()))
start2 = tuple(map(int, input("Введите начальную позицию черного коня: ").split()))

min_moves, meeting_point = find_min_moves(board_size, start1, start2)

if min_moves == -1:
    print("Кони не могут встретиться")
else:
    print("Минимальное число ходов для встречи:", min_moves)
    print("Координаты клетки встречи:", meeting_point)
