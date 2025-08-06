"""
SWEA_6485 - 삼성시의 버스 노선 - D3

문제 설명
- 버스 노선 N개에서 i번째 버스 노선은 번호가 Ai 이상 Bi 이하인 정류장만 다닌다.
- P개의 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는지 구하라.
"""

T = int(input())
for case in range(T):
    N = int(input())
    count_lst = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            count_lst[i] += 1

    P = int(input())
    lst_c = []
    for _ in range(P):
        c = int(input())
        lst_c.append(c)

    print(f'#{case+1}', end=' ')
    for num in lst_c:
        print(count_lst[num], end=' ')
    print()


