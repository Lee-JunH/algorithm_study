"""
SWEA_5102 - 노드의 거리 - D2

문제
- V개의 노드와 E개의 간선 정보가 주어진다.
- 출발 노드에서 도착 노드까지 몇 개의 간선을 자나야하는지 출력

출력
- 도착 노드까지의 간선 개수
- 연결 되어 있지 않으면 0 출력

** 노드 간에 순서가 없다

풀이
- DFS와 다르게 BFS 사용해서 풀어볼까
"""

def bfs(start, end):
    my_q = []
    visited = [False for _ in range(V+1)]   # 방문 체크
    distance = [0 for _ in range(V+1)]      # 거리 저장
    my_q.append(start)  # 첫 노드 push
    visited[start] = True   # 체크
    while my_q:
        node = my_q.pop(0)

        for n in my_dict[node]:
            if not visited[n]:
                visited[n] = True
                my_q.append(n)
                distance[n] = distance[node] + 1
                if n == end:      # 골인 지점이면 종료
                    return distance[n]
    return 0


T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    my_dict = {}                        # dict형으로 연결된 경로 저장
    for _ in range(E):
        a, b = map(int, input().split())
        my_dict.setdefault(a,[])        # 노드가 저장되어 있으면
        my_dict[a].append(b)            # 그 노드에 저장
        my_dict.setdefault(b,[])
        my_dict[b].append(a)
    S, G = map(int, input().split())

    print(f'#{case+1} {bfs(S, G)}')