number = 7
sorted_list = [None for _ in range(number)]


def merge(arr, m, middle, n):
    i = m
    j = middle + 1
    k = m

    # 두 i j 레인지 비교해서 작은것 넣기, O(N)
    while i <= middle and j <= n:
        if arr[i] <= arr[j]:
            sorted_list[k] = arr[i]
            i += 1
        else:
            sorted_list[k] = arr[j]
            j += 1
        k += 1

    # sorted list 에 i 혹은 j 다 들어가있으면 나머지 쭉 넣기
    if i > middle:
        for t in range(j, n + 1):
            sorted_list[k] = arr[t]
            k += 1
    else:
        for t in range(i, middle + 1):
            sorted_list[k] = arr[t]
            k += 1

    # sorted_list 에 있는 내용을 arr 에도 옮겨주기, arr 은 재귀 과정중 계속 변경됨
    for t in range(m, n + 1):
        arr[t] = sorted_list[t]


def merge_sort(arr, m, n):
    if m < n:
        middle = (m + n) // 2
        merge_sort(arr, m, middle)
        merge_sort(arr, middle + 1, n)
        merge(arr, m, middle, n)


def main():
    array = [7, 6, 5, 4, 3, 10, 9]
    merge_sort(array, 0, len(array) - 1)
    for n in sorted_list:
        print(n)


main()
