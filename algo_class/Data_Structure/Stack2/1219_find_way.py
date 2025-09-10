"""
SWEA_1219 - 길찾기 - D4

문제
- A 도시에서 B도시로 가는 길이 존재하는지 확인한다.
- A와 B는 숫자 0과 99으로 고정된다.
- 화살표 방향을 거슬러 돌아갈 수는 없다.

출력
- 가능한 경우 1
- 불가능한 경우 0

풀이
- DFS를 구현하여 목표 지점이 존재하는지 확인한다.
"""

def dfs(dict, stack, vis):
    while stack:
        temp = stack.pop()
        if temp in my_dict:
            for node in dict[temp]:
                if vis[node] == 0:
                    vis[node] = 1
                    stack.append(node)
                    dfs(dict, stack, vis)

T = 10
for _ in range(T):
    case, N = map(int, input().split())
    input_data = list(map(int, input().split()))

    my_dict = {}
    for i in range(0, N*2, 2):
        my_dict.setdefault(input_data[i], [])
        my_dict[input_data[i]].append(input_data[i+1])
    my_stack = []
    visited = [0] * 100
    my_stack.append(0)
    visited[0] = 1
    dfs(my_dict, my_stack, visited)
    print(f'#{case} {visited[99]}')
