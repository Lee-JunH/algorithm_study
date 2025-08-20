"""
SWEA_5178 - 노드의 합 - D3

문제
- 완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고,
- 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다.
- 리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장하고
- 지정한 노드 번호에 저장된 값을 출력하라

풀이
- 먼저 입력받은 값을 바로 힙에 넣는다.
- 넣은 값에 대해 더해서 부모 노드에 값을 저장한다.
- 중요한 것은 모든 리프 노드에 대해 동작해야 한다.
- heap[node] = heap[node*2] + heap[node*2 + 1] 이걸 이용해보자
"""

# 재귀로 하면 sum_node(L)로 바로 호출하면 됨
# -> 시간초과
# def sum_node(node):
#     if node <= N and heap[node] != 0:
#         return heap[node]
#     return sum_node(node*2) + sum_node(node*2 + 1)

T = int(input())
for case in range(T):
    N, M, L = map(int, input().split())
    heap = [0] * (N+1)

    # 1.힙에 데이터 입력하기
    for _ in range(M):
        node_num, data = map(int, input().split())
        heap[node_num] = data
    
    # 2.노드의 합 구하기
    for i in range(N, 1, -1):
        heap[i//2] += heap[i]   #부모노드에 자식노드 하나씩 더해주기

    print(f'#{case+1} {heap[L]}')