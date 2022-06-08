from sys import stdin

def solution():
    """
    <Selection Sort (선택 정렬)>
    : 배열의 요소를 비교하여 가장 작은 값(오름차순의 경우)을 앞 인덱스부터 차례로 위치시킨다.
     첫 번쨰 인덱스에 가장 작은 요소를 놓았다면 그 다음 회전에선 두 번째 요소부터 비교하여 가장 작은 요소를 찾아 두 번째 인덱스에 놓는다.
     시간복잡도 O(N^2)
    """
    arr = list(stdin.readline())

    for i in range(len(arr)):
        max_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]       
    print(''.join(arr))

solution()
