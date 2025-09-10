"""
SWEA_5178 - 노드의 합 - D3

문제
- 완전 이진 트리의 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다.

출력
- 지정한 노드 번호에 저장된 값을 출력

풀이
- 자식노드의 값을 부모노드에 하나씩 더해주자.
"""

T = int(input())
for case in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        node_num, data = map(int, input().split())
        tree[node_num] = data
    
    for i in range(N, 1, -1):
        parent = i // 2
        tree[parent] += tree[i]

    print(f'#{case+1} {tree[L]}')