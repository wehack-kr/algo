import sys

N = int(sys.stdin.readline())
serial = [int(sys.stdin.readline()) for _ in range(N)]


def bubble_sort():
    end = len(serial) - 1
    while end > 0:
        last_swapped = 0
        for i in range(end):
            if serial[i] > serial[i + 1]:
                serial[i], serial[i + 1] = serial[i + 1], serial[i]
                last_swapped = i
        end = last_swapped

    for n in serial:
        print(n)


def insertion_sort():
    for i in range(1, N):
        j = i
        while j > 0 and serial[j - 1] > serial[j]:
            serial[j], serial[j - 1] = serial[j - 1], serial[j]
            j -= 1

    for n in serial:
        print(n)


def selection_sort():
    for i in range(N):
        min_idx = i
        for j in range(i, N):
            if serial[j] < serial[min_idx]:
                min_idx = j

        serial[i], serial[min_idx] = serial[min_idx], serial[i]

    for n in serial:
        print(n)


# bubble_sort()
# insertion_sort()
selection_sort()  # 선택정렬이 가장 빨리 풀림
