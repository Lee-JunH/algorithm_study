"""
SWEA_5105 - 미로의 거리 - D3

문제 설명
- NxN 미로에서 출발지와 목적지가 주어진다.
- 이 때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 계산하라
출력
- 경로가 있는 경우 최소 칸수
- 경로가 없는 경우 0
풀이
-
"""


def backtrack(miro, N, queue, visited, count):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    global optimal

    while queue:
        row, col = queue.pop(0)
        for dir in range(4):
            nr = row + dr[dir]
            nc = col + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] == 1 or miro[nr][nc] == '1':
                continue
            if miro[nr][nc] == '3':
                if optimal < count:
                    optimal = count
                    break
            visited[nr][nc] = 1
            queue.append((nr, nc))
            backtrack(miro, N, queue, visited, count+1)
            count = 0


T = int(input())
for case in range(T):
    N = int(input())
    miro = [list(input().strip()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    my_queue = []

    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                my_queue = [(i, j)]
                visited[i][j] = 1
                break

    optimal = 0
    backtrack(miro, N, my_queue, visited, 0)
    print(f'#{case+1} {optimal}')

