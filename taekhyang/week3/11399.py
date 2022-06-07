import sys


N = int(sys.stdin.readline())
serial = list(map(int, sys.stdin.readline().split(' ')))


def insertion_sort():
    for i in range(1, N):
        j = i
        while j > 0 and serial[j - 1] > serial[j]:
            serial[j], serial[j - 1] = serial[j - 1], serial[j]
            j -= 1

    wait_time_sum = 0
    for i in range(len(serial)):
        wait_time_sum += sum(serial[:i+1])
    print(wait_time_sum)


def bubble_sort():
    end = N - 1
    while end > 0:
        last_swapped = 0
        for i in range(end):
            if serial[i] > serial[i + 1]:
                serial[i], serial[i + 1] = serial[i + 1], serial[i]
                last_swapped = i
        end = last_swapped

    wait_time_sum = 0
    for i in range(len(serial)):
        wait_time_sum += sum(serial[:i + 1])
    print(wait_time_sum)


def selection_sort():
    for i in range(N):
        min_idx = i
        for j in range(i, N):
            if serial[j] < serial[min_idx]:
                min_idx = j

        serial[i], serial[min_idx] = serial[min_idx], serial[i]

    wait_time_sum = 0
    for i in range(len(serial)):
        wait_time_sum += sum(serial[:i + 1])
    print(wait_time_sum)


# insertion_sort()
# bubble_sort()
selection_sort()  # 선택정렬이 가장 빠르게 통과됨
