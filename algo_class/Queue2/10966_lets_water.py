"""
SWEA_10966 - 물놀이를 가자 - D4

문제
- NxM크기의 격자에 위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 'W' 땅이면 'L'
- 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하여 다른 칸으로 이동할 수 있다.
- 땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하라.

출력
- 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력하라

풀이
- 모든 L에 대해 W로의 최소 거리를 찾아 합하는 문제이다.
"""

from collections import deque

T = int(input()) 
for case in range(T):
    N, M = map(int, input().split())
    water = [list(input().strip()) for _ in range(N)]

    vis = [[-1 for _ in range(M)] for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    my_q = deque()
    for i in range(N):
        for j in range(M):
            if water[i][j] == 'W':
                my_q.append((i, j))
                vis[i][j] = 0

    while my_q:
        r, c = my_q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr >= N or nr < 0 or nc < 0 or nc >= M:
                continue
            if vis[nr][nc] == -1:
                vis[nr][nc] = vis[r][c] + 1
                my_q.append((nr, nc))

    result = 0
    for i in range(N):
        for j in range(M):
            if water[i][j] == 'L':
                result += vis[i][j]
    print(f'#{case+1} {result}')
