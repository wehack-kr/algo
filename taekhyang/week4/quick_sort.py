arr = [4, 1, 2, 3, 5]


def quick_sort(data: list, start: int, end: int):
    """
        재귀 과정동안 메모리 잡아먹지 않고 한번 선언한 arr 의 인덱스만 바꿔줘서 메모리 효율이 좋음, but 가독성이 조금 안좋음
    """
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end

    while i <= j:  # i 와 j 가 엇갈리기 전까지, pivot 값이 변경되면 새로운 pivot 값 두개가 생기기 때문에
        # pivot 값보다 큰 값을 만날 때 까지
        while i < end and data[pivot] >= data[i]:
            i += 1

        # pivot 값보다 작은 값을 만날 때 까지  j >= start 이면 j 가 0 일 때 다음 스텝에서 j 는 -1 이 되기 떄문에 j > start 가 되어야 함
        while j > start and data[pivot] <= data[j]:
            j -= 1

        if i >= j:  # 엇갈린 상태 or i == j 이면 pivot 값과 j 값 (작은 값) 교체
            data[pivot], data[j] = data[j], data[pivot]
        else:
            data[i], data[j] = data[j], data[i]  # 엇갈리지 않은 상태면 i, j 교체

    print(data)
    # j 는 새로운 pivot 값
    quick_sort(data, start, j - 1)  # pivot 값 왼쪽
    quick_sort(data, j + 1, end)  # pivot 값 오른쪽


def quick_sort_2(data):
    """
        재귀 과정동안 `left`, `right` 변수에 리스트가 계속 할당되기떄문에 메모리 측면에서 좋진 않지만 가독성 굳
    """
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quick_sort_2(left) + [pivot] + quick_sort_2(right)


def main():
    quick_sort(arr, 0, len(arr) - 1)
    return arr


def main_2():
    result = quick_sort_2(arr)
    return result


print(main_2())
