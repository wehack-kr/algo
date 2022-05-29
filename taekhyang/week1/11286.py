import sys
import heapq


N = int(sys.stdin.readline())


def solution():
    heap = []
    for _ in range(N):
        n = int(sys.stdin.readline())
        val = (abs(n), n)
        if n != 0:
            heapq.heappush(heap, val)
        else:
            if not heap:
                print(0)
                continue

            smallest = heapq.heappop(heap)[1]
            print(smallest)


solution()