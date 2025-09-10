"""
SWEA_4881 - 배열 최소 합 - D2

문제
- NxN 배열에 숫자가 들어있다. 한 줄에 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
- 단, 세로로 같은 줄에서 2개 이상의 숫자를 고를 수 없다.

출력
- 숫자를 골랐을 때의 최소 합

풀이
- backtrak을 이용해서 풀어보기
"""


def backtrack(index, N, sum_v):
    global min_v

    if index == N:
        if min_v > sum_v:
            min_v = sum_v
    elif min_v < sum_v:
        return
    else:
        for i in range(index, N):
            check[index], check[i] = check[i], check[index]     # 자리교환
            backtrack(index+1, N, sum_v + num[index][check[index]])
            check[index], check[i] = check[i], check[index]     # 원상복구


T = int(input())
for case in range(T):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    check = [a for a in range(N)]
    min_v = 100
    backtrack(0, N, 0)
    print(f'#{case+1} {min_v}')

