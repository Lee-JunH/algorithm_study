"""
SWEA_4871 - 그래프 경로 - D2

문제
- V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프가 있다.
- 특정한 2개의 노드에 경로가 존재하는지 확인
    - 간선으로 연결되지 않은 경우도 있다.

풀이
- 간선에 대한 정보를 딕셔너리로 저장한다.
- DFS로 도착지점을 만나면 1을 반환하는 함수를 만든다.
"""

def dfs(vis, stack):
    while stack:
        temp = stack.pop()
        for node in gansun[temp]:
            if vis[node] == 0:
                vis[node] = 1
                if node == G:
                    return 1
                stack.append(node)
                dfs(vis, stack)


T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    gansun = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        gansun[a].append(b)
    S, G = map(int, input().split())
    
    visited = [0] * (V+1)
    my_stack = []
    my_stack.append(S)
    visited[S] = 1
    dfs(visited, my_stack)
    result = 0
    if visited[G] == 1:
        result = 1
    print(f'#{case+1} {result}')