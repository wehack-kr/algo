from sys import stdin


N, M = map(int, stdin.readline().split(' '))
serial = list(map(int, stdin.readline().split(' ')))

input_list = list()
for _ in range(M):
    i, j = map(int, stdin.readline().split(' '))
    input_list.append((i, j))


def solution():
    range_sum_list = [0]
    for i in range(len(serial)):
        range_sum_list.append(range_sum_list[i] + serial[i])

    for i, j in input_list:
        behind = range_sum_list[j]
        front = range_sum_list[i - 1]

        total = behind - front
        print(total)


solution()
