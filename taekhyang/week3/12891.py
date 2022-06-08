import sys

from collections import Counter, deque


total_length, target_length = map(int, sys.stdin.readline().split(' '))
dna = sys.stdin.readline()

alphabet_count_list = list(map(int, sys.stdin.readline().split(' ')))
alphabet_dict = dict(
    A=alphabet_count_list[0],
    C=alphabet_count_list[1],
    G=alphabet_count_list[2],
    T=alphabet_count_list[3]
)


def solution_with_counter():
    password = deque([s for s in dna[:target_length]])
    alphabet_counter = Counter(alphabet_dict)
    current_counter = Counter(password)
    valid_cnt = 1 if not (alphabet_counter - current_counter) else 0

    for i in range(target_length, total_length):
        to_remove = password.popleft()
        to_insert = dna[i]
        password.append(to_insert)
        current_counter = current_counter - Counter(to_remove) + Counter(to_insert)

        if not (alphabet_counter - current_counter):
            valid_cnt += 1

    print(valid_cnt)


def solution_without_counter():
    password = [s for s in dna[:target_length]]
    for k in password:
        alphabet_dict[k] -= 1

    valid_cnt = 0
    is_valid = True
    for k in alphabet_dict:
        if alphabet_dict[k] > 0:
            is_valid = False
            break

    valid_cnt += 1 if is_valid else 0

    for i in range(target_length, total_length):
        alphabet_dict[dna[i - target_length]] += 1
        alphabet_dict[dna[i]] -= 1
        is_valid = True
        for k in alphabet_dict:
            if alphabet_dict[k] > 0:
                is_valid = False
                break

        valid_cnt += 1 if is_valid else 0
    print(valid_cnt)


solution_without_counter()
