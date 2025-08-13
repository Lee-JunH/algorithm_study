"""
SWEA_5122 - 수열 편집 - D4

문제
- N개의 10억 이하 자연수로 이뤄진 수열이 있다.
- 이 수열은 완성된 것이 아니라 M번의 편집을 거쳐 완성된다.
- 조건
    - I a b : a번 인덱스 앞에 b를 추가하고, 한 칸 씩 뒤로 이동
    - D a : a번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동
    - C a b : a번 인덱스 자리를 b로 변경
출력
- L의 데이터 출력
- 편집이 끝난 후 L이 존재하지 않으면 -1
"""

# 기본 연결 리스트 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data    # 데이터 저장
        self.next = None    # 다음 노드 주소 저장

def link_init(input):
    head = Node(input[0])
    current = head
    for i in range(1, N):
        new_node = Node(input_data[i])          # new_node 생성
        current.next = new_node                 # 현재노드의 다음 노드를 new_node로 연결
        current = new_node                      # 현재를 new_node로 변경
    return head

def link_insert(head, index, data):
    cur = head
    for _ in range(index-1):
        cur = cur.next
    
    temp = cur.next     # cur의 다음 값 임시 저장
    new_node = Node(data)   # new_node를 data로 생성
    cur.next = new_node     # cur의 다음 주소를 new_node로 변경
    new_node.next = temp    # new_node의 다음 주소를 임시 저장했던 temp로 변경

def link_delete(head, index):
    cur = head
    for _ in range(index-1):    # 지워야할 인덱스 이전 위치로 이동
        cur = cur.next
    temp = cur.next             # 지우는 인덱스 임시 저장
    cur.next = cur.next.next    # 지우고 다음으로 바로 연결
    temp = None                 # 지운 노드의 next를 None으로 만들어 지우기

def link_change(head, index, data):
    cur = head
    for _ in range(index):  # 변경할 인덱스로 이동
        cur = cur.next
    cur.data = data         # 변경

T = int(input())
for case in range(T):
    N, M, L = map(int, input().split()) # N: 수열의 길이, M: 추가 횟수, L: 출력 인덱스
    input_data = list(map(int, input().split()))

    # 1. 연결 리스트 만들기
    head = link_init(input_data)
    
    # 2. I, D, C 작업하기
    count = 0   # 추가 또는 제거 체크
    for _ in range(M):
        operation = list(input().split())
        if operation[0] == 'I':
            count += 1
            link_insert(head, int(operation[1]), int(operation[2]))
        elif operation[0] == 'D':
            count -= 1
            link_delete(head, int(operation[1]))
        elif operation[0] == 'C':
            link_change(head, int(operation[1]), int(operation[2]))
    
    # 3. 출력하기
    print(f'#{case+1}', end= ' ')
    if N + count <= L:
        print(-1)
    else:
        cur = head
        for _ in range(L):
            cur = cur.next
        print(cur.data)