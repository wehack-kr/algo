import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
material_ids = list(map(int, sys.stdin.readline().split(' ')))
material_ids.sort()


def solution():
    partial_sum = material_ids[0] + material_ids[-1]
    start = 0
    end = N - 1
    matched_count = 0

    while end - start >= 1:
        if partial_sum == M:
            matched_count += 1
            start += 1
            end -= 1
        elif partial_sum > M:
            end -= 1
        elif partial_sum < M:
            start += 1
        partial_sum = material_ids[start] + material_ids[end]
    print(matched_count)


solution()
