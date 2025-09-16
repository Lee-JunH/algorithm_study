"""
SWEA_5251 - 최소 이동 거리 - D4

문제
- A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0~N까지의 번호가 붙어있다.
- 구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 부터 N번 까지의 최소거리를 구하기
"""

from heapq import heappush, heappop

def djikstra():
    my_hq = [(0,0)]
    while my_hq:
        cur, distance = heappop(my_hq)
        if distance > dist[cur]:
            continue
        for next, d in node[cur]:
            if distance + d < dist[next]:
                dist[next] = distance + d
                heappush(my_hq, (next, distance + d))

T = int(input())
for case in range(T):
    N, E = map(int, input().split())

    node = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        node[s].append((e,w))
    
    dist = [float('inf') for _ in range(N+1)]
    dist[0] = 0
    djikstra()

    print(f'#{case+1} {dist[N]}')