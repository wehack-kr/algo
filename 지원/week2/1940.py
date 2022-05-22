from sys import stdin

def solution():
    N, M = int(stdin.readline()), int(stdin.readline())
    numbers = sorted(list(map(int, stdin.readline().split())))

    start, end = 0, N-1
    result = 0

    while start < end:
        sum = numbers[start] + numbers[end]

        if sum == M:
            result += 1
            end -= 1
        elif sum < M:
            start += 1
        elif sum > M:
            end -= 1
        
    return result

print(solution())