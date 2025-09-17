"""
SWEA_5249 - 최소 신장 트리 - D4

문제
- 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
- 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
- 0~V까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때
- 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 문제
"""

from heapq import heappush, heappop, heapify

def search(start, dist):
    global result

    lst = []
    for next in node[start]:
        lst.append(next)
    visited[0] = 1

    heapify(lst)
    while lst:
        weight, now = heappop(lst)

        if not visited[now]:
            result += weight
            visited[now] = 1
            for weight, next in node[now]:
                if not visited[next]:
                    heappush(lst, (weight, next))

T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        node[n1].append((w, n2))
        node[n2].append((w, n1))
    
    visited = [0] * (V + 1)
    result = 0
    search(0,0)

    print(f'#{case+1} {result}')