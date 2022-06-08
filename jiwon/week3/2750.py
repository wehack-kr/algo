from sys import stdin

def solution():
    """
    <Bubble Sort (버블 정렬)>
    : 인접한 요소와 비교하며 정렬한다.
     첫 번째 수를 인접한 두 번째 수와 비교하여 더 클 때(오름차순의 경우) 자리를 교환한다.
     다시 두 번째 수는 세 번째 수와 비교하고 마지막 수까지 비교가 끝나면 맨 뒤에 가장 큰 수가 위치하게 된다.
     따라서 각 회전마다 비교할 데이터가 하나씩 줄어들게 된다.
     시간복잡도 O(N^2)
    """
    N = int(stdin.readline())
    arr = [int(stdin.readline()) for _ in range(N)]

    for i in range(N - 1):
        min_index = i

        for j in range(i + 1, N):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    for n in arr:
        print(n)
        
solution()
