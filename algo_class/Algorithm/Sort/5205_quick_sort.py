"""
SWEA_5205 - 퀵 정렬 - D3

문제
- 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 문제
"""

def partition(lst, l, r):
    pivot = lst[l]
    i = l
    j = r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j

def quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quick_sort(lst, l, s-1)
        quick_sort(lst, s+1, r)

T = int(input())
for case in range(T):
    N = int(input())
    quick = list(map(int, input().split()))

    quick_sort(quick,0,N-1)

    print(f'#{case+1} {quick[N//2]}')