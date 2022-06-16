import sys
from collections import deque


def redix_sort(nums):
    max_num = max(nums)
    max_digit = len(str(max_num))

    bucket = [deque() for _ in range(10)]  # 10 진수
    for i in range(1, max_digit + 1):
        for n in nums:
            digit = n % (10 ** i)
            bucket[digit].append(n)

        nums = list()
        for d in bucket:
            while d:
                popped = d.popleft()
                nums.append(popped)
    return nums


def redix_sort_2():
    """
        왜 메모리초과?
    """
    N = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(N)]

    max_num = max(nums)
    max_digit = len(str(max_num))

    for i in range(1, max_digit + 1):
        bucket = [dict() for _ in range(10)]  # 10 진수
        for n in nums:
            digit = n % (10 ** i)
            bucket[digit].setdefault(n, 0)
            bucket[digit][n] += 1

        nums = list()
        for d in bucket:
            for k, v in d.items():
                nums.extend([k] * v)

    for n in nums:
        print(n)


def counting_sort():
    """
    10000 보다 작거나 같은 자연수
    """
    N = int(sys.stdin.readline())
    bucket = [0] * 10001
    for _ in range(N):
        bucket[int(sys.stdin.readline())] += 1

    for idx, cnt in enumerate(bucket):
        for _ in range(cnt):
            print(idx)


def solution():
    counting_sort()
    # redix_sort_2()


solution()
