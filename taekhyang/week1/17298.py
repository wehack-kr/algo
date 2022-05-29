import sys

from collections import deque


N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split(' ')))


def solution():
    answer = [-1 for _ in range(N)]
    stack = deque()

    for idx in range(N - 1):
        if sequence[idx] < sequence[idx + 1]:
            answer[idx] = sequence[idx + 1]
            while stack and sequence[stack[-1]] < sequence[idx + 1]:
                answer[stack[-1]] = sequence[idx + 1]
                stack.pop()
        else:
            stack.append(idx)
    print(*answer)


solution()
