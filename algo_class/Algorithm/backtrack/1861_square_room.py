"""
SWEA_1861 - 정사각형 방 - D4

문제
- N^2개의 방이 NxN 형태로 있다.
- 어떤 방에 있을 때, 상하좌우로 이동 가능하다.
- 이동하는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
- 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 문제

풀이
- 각 위치부터 dfs를 하고 각 크기를 저장
"""

def backtrack(r, c):
    global cnt
    global start

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if room[r][c] + 1 == room[nr][nc]:
            cnt += 1
            visited[nr][nc] = 1
            backtrack(nr, nc)
            break
    my_room[start] = cnt

T = int(input())
for case in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    my_room = [0 for _ in range(N**2+1)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt = 1
                start = room[i][j]
                backtrack(i, j)

    max_d = max(my_room)
    for i in range(N+1):
        if my_room[i] == max_d:
            print(f'#{case+1} {i} {max_d}')
            break