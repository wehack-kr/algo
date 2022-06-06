from sys import stdin

# Bubble Sort
def solution():
    N = int(stdin.readline())
    numbers = [int(stdin.readline()) for _ in range(N)]

    for i in range(N - 1):
        min_index = i

        for j in range(i + 1, N):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    for n in numbers:
        print(n)
        
solution()