from sys import stdin

def solution():
    N = int(stdin.readline())
    numbers = sorted(list(map(int, stdin.readline().split())))
    result = 0

    for n in numbers:
        truncated_numbers = numbers.copy()
        truncated_numbers.remove(n)

        start, end = 0, len(truncated_numbers) - 1

        while start < end:
            sum = truncated_numbers[start] + truncated_numbers[end]

            if n == sum:
                result += 1
                break
            if n < sum:
                end -= 1
            elif n > sum:
                start += 1

    return result

print(solution())