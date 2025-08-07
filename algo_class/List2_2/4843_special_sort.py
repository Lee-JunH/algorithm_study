"""
SWEA_4843 - 특별한 정렬 - D3

문제 설명
N개의 정수가 주어지면 가장 큰 수, 가장 작은  수, 2번째 작은 수, ...와 같이 정렬하고 10개 출력해라
"""

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    sort_lst = []

    while True:
        i = 0
        mx = 1
        mn = 100
        while i < len(lst):
            if mx < lst[i]:
                mx = lst[i]
            if mn > lst[i]:
                mn = lst[i]
            i += 1
        lst.remove(mx)
        sort_lst.append(mx)
        if len(sort_lst) == N:
            break
        lst.remove(mn)
        sort_lst.append(mn)
        if len(sort_lst) == N:
            break
    print(f'#{case+1} ', end='')
    for i in range(10):
        print(sort_lst[i], end=' ')
    print()

