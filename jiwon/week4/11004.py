from sys import stdin

def solution():
    """
    <Quick Sort (퀵 정렬)>
    : 
     시간복잡도 
     평균: O(NlogN)
     최악: O(N^2)
    """
    N, K = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    
    def partition(left, right):
        pivot = arr[(left + right) // 2]

        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left
        
    def quick_sort(left, right):
        if right <= left:
            return
          
        mid = partition(left, right)

        quick_sort(left, mid - 1)
        quick_sort(mid, right)

    quick_sort(0, N - 1)

    print(arr[K])

solution()
