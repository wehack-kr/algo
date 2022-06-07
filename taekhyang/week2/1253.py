import sys


N = int(sys.stdin.readline())
serial = list(map(int, sys.stdin.readline().split(' ')))
serial.sort()


def solution():
    matched_count = 0

    for target_num in serial:
        serial_except_target = serial[:]
        serial_except_target.remove(target_num)

        start = 0
        end = N - 2
        partial_sum = serial_except_target[start] + serial_except_target[end]

        while end - start >= 1:
            if partial_sum > target_num:
                end -= 1
            elif partial_sum == target_num:
                end -= 1
                start += 1
                matched_count += 1
                break
            else:
                start += 1

            partial_sum = serial_except_target[start] + serial_except_target[end]

    print(matched_count)


solution()
