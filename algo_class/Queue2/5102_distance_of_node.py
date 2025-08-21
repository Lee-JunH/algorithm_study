"""
SWEA_5102 - 노드의 거리 - D2

문제
- V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
- 주어진 출발 노드에서 최소 몇개의 간선을 지나면 도착 노드에 갈 수 있는지 계산하라

풀이
- 방향성이 없다고 했기 때문에 양방향으로 이동 가능하다.
- 이를 이용해 딕셔너리에 간선 정보를 저장하고 큐를 이용해 구현하자
"""

from collections import deque

def bfs_node(q):
    while q:
        cur = q.popleft()
        for node in my_d[cur]:
            if vis[node] != 1:
                vis[node] = 1
                q.append(node)
                dis[node] = dis[cur] + 1
                if node == G:
                    return dis[G]
    return 0

T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    my_d = {}
    for i in range(E):
        n1, n2 = map(int, input().split())
        my_d.setdefault(n1, [])
        my_d[n1].append(n2)   # 양쪽 다 넣어준다.
        my_d.setdefault(n2, [])
        my_d[n2].append(n1)
    S, G = map(int, input().split())

    my_q = deque()
    vis = [0 for _ in range(V+1)]
    dis = [0 for _ in range(V+1)]
    my_q.append(S)
    vis[S] = 1

    print(f'#{case+1} {bfs_node(my_q)}')