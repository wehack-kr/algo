import sys

from collections import deque


N = int(sys.stdin.readline())


def solution():
    stack = deque([n for n in range(1, N + 1)])

    while len(stack) > 1:
        stack.popleft()
        stack.append(stack.popleft())
    print(stack[0])


solution()
