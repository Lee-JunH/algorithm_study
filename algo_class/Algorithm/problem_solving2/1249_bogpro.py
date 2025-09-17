"""
SWEA_1249 - 보급로 - D4

문제
- 공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.
- 도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.
- 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하는 문제
"""

from heapq import heappop, heappush

def dijkstra():
    dists = [[21e8] * N for _ in range(N)]
    dists[0][0] = 0

    pq = [(0,0,0)]
    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            new_dist = dist + time[ny][nx]
            
            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))
    return dists[N-1][N-1]


T = int(input())
for case in range(T):
    N = int(input())
    time = [list(map(int, input())) for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    result = dijkstra()
    print(f'#{case+1} {result}')