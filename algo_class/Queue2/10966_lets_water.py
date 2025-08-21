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

def bfs(start, end):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    vis = [[0 for _ in range(M)] for _ in range(N)]
    my_q = deque()
    my_q.append([start, end])
    dis = [[0 for _ in range(M)] for _ in range(N)]

    while my_q:
        r, c = my_q.popleft()
        vis[r][c] = 1
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr >= N or nr < 0 or nc < 0 or nc >= M or vis[nr][nc] == 1:
                continue
            if water[nr][nc] == 'W':
                return dis[r][c] + 1
            vis[nr][nc] = 1
            dis[nr][nc] = dis[r][c] + 1
            my_q.append([nr, nc])
    return 0

T = int(input()) 
for case in range(T):
    N, M = map(int, input().split())
    water = [list(input().strip()) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            if water[i][j] == 'L':
                result += bfs(i, j)
    
    print(f'#{case+1} {result}')

