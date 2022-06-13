import sys


N, K = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))
answer_index = K - 1


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end

    while i <= j:
        while i < end and arr[pivot] >= arr[i]:
            i += 1

        while j > start and arr[pivot] <= arr[j]:
            j -= 1

        if i >= j:
            arr[pivot], arr[j] = arr[j], arr[pivot]
        else:
            arr[i], arr[j] = arr[j], arr[i]

    if answer_index < j:
        quick_sort(arr, start, j - 1)
    elif answer_index > j:
        quick_sort(arr, j + 1, end)
    else:
        return


def solution():
    quick_sort(A, 0, N - 1)
    print(A[answer_index])


solution()
