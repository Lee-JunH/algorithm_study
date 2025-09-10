"""
SWEA_18795 - 퀵 정렬 연습 - D2

문제
- 퀵정렬 하시오
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
    lst = list(map(int, input().split()))

    quick_sort(lst,0,len(lst)-1)

    print(f'#{case+1}', end=' ')
    print(*lst)