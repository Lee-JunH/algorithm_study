"""
SWEA_5176 - 이진탐색 - D2

문제
- 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
- 이진 탐색 트리는 항상 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브 트리의 루트 이다.
- N이 주어졌을 때 이진 탐색 트리의 루트에 저장된 값과
- N/2번 노드 (N이 홀수면 소수점 버림)에 저장된 값을 출력

풀이
1. 이진트리는 왼쪽과 오른쪽 노드를 자식으로 가지는 것을 이용해보자
2. index는 왼쪽은 부모의 *2, 오른쪽은 부모의 *2 + 1인 것을 이용
3. 중위 순회 방식으로 값들을 저장하고 마지막에 index로 출력한다.
"""

def inorder_traversal(cur):    # 중위 순회
    global cnt

    left_i = 2*cur      # 왼쪽 인덱스
    right_i = 2*cur + 1 # 오른쪽 인덱스
    
    if left_i <= N:
        inorder_traversal(left_i)    # 왼쪽아래로 먼저 이동
    tree[cur] = cnt
    cnt += 1
    if right_i <= N:
        inorder_traversal(right_i)   # 오른쪽아래로 이동

T = int(input())
for case in range(T):
    N = int(input())

    tree = [0] * (N + 1)  # tree의 노드 개수는 N개
    cnt = 1
    inorder_traversal(1)

    print(f'#{case+1} {tree[1]} {tree[N//2]}')

