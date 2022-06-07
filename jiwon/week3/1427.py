from sys import stdin

# Selection Sort
def solution():
    numbers = list(stdin.readline())

    for i in range(len(numbers)):
        max_index = i

        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j

        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]       
    print(''.join(numbers))

solution()