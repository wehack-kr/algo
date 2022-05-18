import sys


N = int(sys.stdin.readline())
target_serial = [int(sys.stdin.readline()) for _ in range(N)]


def solution():
    push_pop_order = list()
    serial = [n for n in range(1, N + 1)]
    stack = list()
    answer = list()
    target = target_serial[:]
    no_flag = False

    while True:
        if stack and stack[-1] == target[0]:
            answer.append(stack.pop(-1))
            target.pop(0)
            push_pop_order.append('-')
            if not stack and not target:
                break
        else:
            if serial:
                stack.append(serial.pop(0))
                push_pop_order.append('+')
            else:
                print('NO')
                no_flag = True
                break

    if not no_flag:
        for behavior in push_pop_order:
            print(behavior)


solution()
