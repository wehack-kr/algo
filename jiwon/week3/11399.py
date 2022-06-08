
def solution():
    """
    <Insertion Sort (삽입 정렬)>
    : 처음 Key는 두 번째 인덱스부터 시작함.(첫 번째 배열은 이미 정렬된 배열이기 때문)
     앞의 이미 정렬된 배열의 요소들과 비교하며 자리를 찾고 삽입한다.
     삽입 시 기존 자료는 이동이 필요함.
     시간복잡도 O(N^2)
    """
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().split(' ')))
    result_sum = 0

    for i in range(1, N):
        curr = arr[i]
        for j in reversed(range(0, i)):
            if arr[j] > curr:
                arr[j], arr[j + 1] = curr, arr[j]

    for i in range(len(arr)):
        result_sum += sum(arr[:i + 1])
    print(result_sum)

solution()
