"""
SWEA_5105 - 미로의 거리 - D3

문제
- NxN 크기의 미로에서 출발지와 목적지가 주어진다.
- 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 계산하라
- 1은 벽, 0은 통로, 2는 출발점이다.

풀이
- 이것도 큐를 이용한 dfs를 시행하면서 최소 경로 횟수를 계산한다.
"""

from collections import deque

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j
    return 0,0

def bfs_maze():
    while my_q:
        r, c = my_q.popleft()
        vis[r][c] = 1
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr >= N or nr < 0 or nc < 0 or nc >= N:
                continue
            if maze[nr][nc] == 1 or vis[nr][nc] == 1:
                continue
            if maze[nr][nc] == 3:
                return dis[r][c]
            vis[nr][nc] = 1
            dis[nr][nc] = dis[r][c] + 1
            my_q.append([nr, nc])
    return 0

T = int(input())
for case in range(T):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    vis = [[0 for _ in range(N)] for _ in range(N)]
    my_q = deque()
    dis = [[0 for _ in range(N)] for _ in range(N)]
    my_q.append(find_start())

    print(f'#{case+1} {bfs_maze()}')