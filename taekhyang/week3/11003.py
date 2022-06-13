import sys
import heapq


N, L = map(int, sys.stdin.readline().split(' '))
serial = list(map(int, sys.stdin.readline().split(' ')))


def solution():
    heap = list()
    num_counter = dict()
    answer = list()
    for i in range(N):
        num_counter.setdefault(serial[i], 0)
        num_counter[serial[i]] += 1

        heapq.heappush(heap, serial[i])
        if i < L:
            answer.append(str(heap[0]))
        else:
            num_counter[serial[i - L]] -= 1
            while True:
                if num_counter[heap[0]] > 0:
                    answer.append(str(heap[0]))
                    break
                else:
                    heapq.heappop(heap)

    print(' '.join(answer))


solution()
