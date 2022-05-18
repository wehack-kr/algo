import sys


N = int(sys.stdin.readline())


def solution():
    start = 0
    end = 0
    matched_cnt = 0

    while end <= N:
        partial_sum = end * (end + 1) / 2 - start * (start + 1) / 2 + start  # sum of 1 ~ n -> n(n + 1) / 2 
        if partial_sum > N:
            start += 1
        else:
            if partial_sum == N:
                matched_cnt += 1
            end += 1

    print(matched_cnt)


solution()
