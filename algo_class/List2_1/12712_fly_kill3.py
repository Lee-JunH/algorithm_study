"""
SWEA_12712 - 파리퇴치3 - D2

문제
- '+'혹은 'x' 형태로 분사되는 스프레이를 분사한 경우 최대 파리 수 를 구하라

풀이
- 자기 위치에서 부터 인덱스를 넘어가기 전까지 합을 구하기
- x형태인 경우
"""


def cross_spray(arr, i, j, M):
    sum_cross = arr[i][j]
    for iter in range(1, M):
        for r, c in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
            nr = i + r * iter
            nc = j + c * iter
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            sum_cross += arr[nr][nc]
    return sum_cross


def plus_spray(arr, i, j, M):
    sum_plus = arr[i][j]
    for iter in range(1, M):
        for r, c in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = i + r * iter
            nc = j + c * iter
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            sum_plus += arr[nr][nc]
    return sum_plus


T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum_plus = plus_spray(fly, i, j, M)
            sum_cross = cross_spray(fly, i, j, M)
            if max_sum < sum_plus:
                max_sum = sum_plus
            if max_sum < sum_cross:
                max_sum = sum_cross
    print(f'#{case+1} {max_sum}')

