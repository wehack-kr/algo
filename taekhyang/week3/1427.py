import sys


serial = list(sys.stdin.readline())


def selection_sort():
    """
        선택정렬 내림차순으로 하려면 min_idx 대신 max_idx 를 찾으면 됨
    """
    for i in range(len(serial) - 1):
        max_idx = i
        for j in range(i, len(serial)):
            if serial[j] > serial[max_idx]:
                max_idx = j
        serial[i], serial[max_idx] = serial[max_idx], serial[i]
    print(''.join(serial))


def bubble_sort():
    """
        버블정렬 또한 내림차순으로 하려면 대소비교만 반대로 해주면 됨
    """
    end = len(serial) - 1
    while end > 0:
        last_swapped = 0
        for i in range(end):
            if serial[i] < serial[i + 1]:
                serial[i], serial[i + 1] = serial[i + 1], serial[i]
                last_swapped = i
        end = last_swapped
    print(''.join(serial))


def insertion_sort():
    for i in range(1, len(serial)):
        j = i
        while j > 0 and serial[j] > serial[j - 1]:
            serial[j], serial[j - 1] = serial[j - 1], serial[j]
            j -= 1
    print(''.join(serial))


selection_sort()  # 선택정렬이 가장 빨리 통과됨
# bubble_sort()
# insertion_sort()
