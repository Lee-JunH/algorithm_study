"""
SWEA_9490 - 풍선팡 - D2

문제
- MxN에 풍선이 있다. 풍선을 터뜨리면 터진 곳의 숫자만큼 상하좌우의 풍선이 터지면서 들어있는 꽃가루가 날린다.
- 날릴 수 있는 꽃가루의 합 중 최대값을 출력하라

출력
- 상하좌우로 그 자리의 수만큼 퍼져나간 꽃가루의 함 중 최대값 출력

풀이
- 그 자리의 수 만큼 반복하여 상하좌우로 이동하여 합을 구하자
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    ballon = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            sum_ballon = ballon[i][j]
            extend = ballon[i][j]
            for k in range(1, extend + 1):
                for dir in range(4):
                    nr = i + dr[dir] * k
                    nc = j + dc[dir] * k
                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue
                    sum_ballon += ballon[nr][nc]
            if sum_ballon > max_sum:
                max_sum = sum_ballon
    print(f'#{case+1} {max_sum}')