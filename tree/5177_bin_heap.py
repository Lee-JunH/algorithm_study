"""
SWEA_5177 - 이진 힙 - D2

문제
- 이진 최소힙은 다음과 같은 특징을 가진다.
    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
    - 부모 노드의 값 < 자식 노드의 값을 유지한다.
    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가
- N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고,
- 마지막 노드의 조상 노드에 저장된 정수의 합을 구하라

출력
- 마지막 노드의 조상 노드에 저장된 정수의 합

풀이
- 이진탐색에서 사용한 것과 같이 왼쪽부터 값을 넣어준다.
""" 

def inorder_traversal(cur):    # 중위 순회
    left_i = 2*cur      # 왼쪽 인덱스
    right_i = 2*cur + 1 # 오른쪽 인덱스
    
    if left_i <= N:
        inorder_traversal(left_i)    # 왼쪽아래로 먼저 이동
    tree[cur] = lst[i]
    i += 1
    if right_i <= N:
        inorder_traversal(right_i)   # 오른쪽아래로 이동

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    tree = [0] * (N+1)
