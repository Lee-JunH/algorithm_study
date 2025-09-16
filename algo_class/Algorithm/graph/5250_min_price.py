"""
SWEA_5250 - 최소 비용 - D3

문제
- 출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달리지기 때문에
- 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.
- 최소 연료 소비량을 출력하는 문제
"""

from heapq import heappush, heappop

T = int(input())
for case in range(T):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    map_fuel = [[float('inf') for _ in range(N)] for _ in range(N)]
    my_heapq = [(0,0,0)]
    vis = set([])

    while my_heapq:
        fuel, r, c = heappop(my_heapq)
        if (r, c) in vis:
            continue
        vis.add((r, c))
        if map_fuel[r][c] > fuel:
            map_fuel[r][c] = fuel
        for dir in range(4): 
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if (nr, nc) in vis:
                continue
            dif = H[nr][nc] - H[r][c]
            if dif < 0: dif = 0
            heappush(my_heapq, (map_fuel[r][c] + dif + 1, nr, nc))

    print(f'#{case+1} {map_fuel[N-1][N-1]}')