number_cnt = int(input())
serial_number = str(input())


def solution_1():
    return sum(map(int, list(serial_number)))


def solution_2():
    total_sum = 0
    for i in range(number_cnt):
        total_sum += int(serial_number[i])

    return total_sum


print(solution_2())
