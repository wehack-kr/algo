from sys import stdin

def solution():
    N = int(stdin.readline())
    numbers = [int(stdin.readline()) for _ in range(N)]
    current_number = 1
    stack, result_list = [], []

    for n in numbers:
        while n >= current_number:
            result_list.append('+')
            stack.append(current_number)
            current_number += 1

        if stack[-1] == n:
            result_list.append('-')
            stack.pop()

    if stack:
        print('NO')
    else:
        print('\n'.join(result_list))

solution()