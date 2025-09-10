"""
SWEA_5204 - 병합 정렬 - D3

문제
- 병합 정렬을 이용해 오른차순으로 정렬하고 L(N//2) 원소를 출력하는 문제
- 추가로 분할했을 때 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력해라.
"""

def merge(lst1, lst2):
    global cnt

    if lst1[-1] > lst2[-1]: # 왼쪽 마지막이 오른쪽 마지막보다 큰 경우
        cnt += 1

    i = 0
    j = 0
    new_lst = []
    while i != len(lst1) and j != len(lst2):
        if lst1[i] < lst2[j]:
            new_lst.append(lst1[i])
            i += 1
        elif lst1[i] == lst2[j]:
            new_lst.extend([lst1[i], lst2[j]])
            i += 1
            j += 1
        else:
            new_lst.append(lst2[j])
            j += 1
    while i < len(lst1):
        new_lst.append(lst1[i])
        i += 1
    while j < len(lst2):
        new_lst.append(lst2[j])
        j += 1
    return new_lst

def merge_sort(lst):
    length = len(lst)
    if length == 1:
        return lst
    a = lst[:length//2]
    b = lst[length//2:]

    lst1 = merge_sort(a)
    lst2 = merge_sort(b)

    return merge(lst1, lst2)

T = int(input())
for case in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0

    new_L = merge_sort(L)

    print(f'#{case+1} {new_L[N//2]} {cnt}')