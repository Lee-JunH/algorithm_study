"""
SWEA_4875 - 미로 - D2

문제
- NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인

출력
- 도착할 수 있으면 1
- 도착할 수 없으면 0

풀이
- 백트랙킹을 이용하여 갈 수 있는지 확인하고 없으면 원래 자리로 돌아와 다른 위치로 이동한다.
"""


def backtracking(stack, visited, maze):
    while stack:
        temp = stack.pop()
        for dir in range(4):
            nr = temp[0] + dr[dir]
            nc = temp[1] + dc[dir]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc] == 1 or maze[nr][nc] == 1:
                continue
            if maze[nr][nc] == 3:
                return 1
            visited[nr][nc] = 1
            stack.append([nr, nc])
    return 0


T = int(input())
for case in range(T):
    N = int(input().strip())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    s_i = 0
    s_j = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s_i = i
                s_j = j
                break
        if maze[i][j] == 2:
            break

    stack = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    stack.append([s_i, s_j])
    result = backtracking(stack, visited, maze)
    print(f'#{case+1} {result}')


