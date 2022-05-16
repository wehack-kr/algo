from sys import stdin


N, M = map(int, stdin.readline().split(' '))


def solution():
    square = list()
    for _ in range(N):
        line = list(map(int, stdin.readline().split(' ')))
        square.append(line)

    sum_square = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            sum_square[i + 1][j + 1] = sum_square[i + 1][j] + sum_square[i][j + 1] - sum_square[i][j] + square[i][j]

    for _ in range(M):
        x1, y1, x2, y2 = list(map(int, stdin.readline().split(' ')))
        total_sum = sum_square[x2][y2]
        subtract_sum = sum_square[x1 - 1][y2] + sum_square[x2][y1 - 1] - sum_square[x1 - 1][y1 - 1]

        square_sum = total_sum - subtract_sum
        print(square_sum)


solution()
