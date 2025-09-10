"""
SWEA_5174 - subtree - D2

문제
- 트리의 일부를 서브 트리라 한다.
- 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내라

풀이
- 입력 노드들을 리스트로 저장하고 시작 지점을 큐에 넣고 자식 노드들을 계속 넣으며 count한다.
"""

from collections import deque

T = int(input())
for case in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    node_lst = [[] for _ in range(E+2)]
    for i in range(0, 2*E, 2):
        node_lst[lst[i]].append(lst[i+1])
    
    # bfs로 모든 노드 확인하기
    my_q = deque()
    my_q.append(N)
    cnt = 1
    while my_q:
        node = my_q.popleft()
        for n in node_lst[node]:
            my_q.append(n)
            cnt += 1
    
    print(f'#{case+1} {cnt}')