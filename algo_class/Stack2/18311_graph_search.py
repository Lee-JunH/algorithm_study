"""
SWEA_18311 - 그래프 탐색 - D2

문제
- 모든 정점을 DFS하여 화면에 탐색 경로를 출력
- 시작 정점은 1
- 정점 탐색시 숫자가 낮은 정점부터 방문한다.

풀이
- DFS를 이용하여 visited를 선언하여 방문여부를 확인하고 스택에 저장한다.
"""

def sort_lst(lst):
    l = len(lst)
    for i in range(l-1, -1, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def dfs(my_stack, vis, result):
    while my_stack:
        temp = my_stack.pop()
        result.append(temp)
        for g in gansun[temp]:
            if vis[g] == 0:
                my_stack.append(g)
                vis[g] = 1
                dfs(my_stack, vis, result)

T = 1
for case in range(T):
    V, E = map(int, input().split())
    node = list(map(int, input().split()))

    visited = [0] * (V+1)
    gansun = {}
    result = []
    for i in range(0,len(node), 2):
        gansun.setdefault(node[i], [])
        gansun[node[i]].append(node[i+1])
        gansun.setdefault(node[i+1], [])
        gansun[node[i+1]].append(node[i])
    for j in gansun:
        sort_lst(gansun[j])
    my_stack = []
    my_stack.append(1)  # 시작 정점 push
    visited[1] = 1
    dfs(my_stack, visited, result)
    print(f'#{case+1}', end=' ')
    for i in range(len(result)):
        if i == len(result) - 1:
            print(result[i])
        else:
            print(result[i], end='-')