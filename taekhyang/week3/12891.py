import sys
from collections import Counter


total_length, target_length = map(int, sys.stdin.readline().split(' '))
dna = list(sys.stdin.readline().replace('\n', ''))

alphabet_count_list = list(map(int, sys.stdin.readline().split(' ')))
alphabet_counter = Counter(dict(A=alphabet_count_list[0], C=alphabet_count_list[1], G=alphabet_count_list[2], T=alphabet_count_list[3]))


def solution():
    password = ''
    current_counter = Counter()
    valid_cnt = 0

    for i in range(total_length):
        if i < target_length:
            to_insert = dna[i]
            password += to_insert

            current_counter += Counter(to_insert)
        else:
            to_remove = password[0]
            to_insert = dna[i]
            password = password[1:]
            password += to_insert

            current_counter = current_counter - Counter(to_remove) + Counter(to_insert)

        if not (alphabet_counter - current_counter):
            valid_cnt += 1
    print(valid_cnt)


solution()