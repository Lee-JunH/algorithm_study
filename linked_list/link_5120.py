"""
SWEA_5108 - 암호 - D4

문제
- 최대 10개인 비밀번호를 찾는 프로그램 찾기
- 조건
    - 1000이하의 숫자 N개, 시작 숫자가 정해지고, 첫 번째 지정 위치가 된다.
    - 지정 위치부터 M번째 칸을 추가한다. 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣는다.
    - 밀려난 칸이 없으면 시작 숫자와 더한다.
    - K회 반복하는데, M칸 전에 마지막 숫자에 이르면 남은 칸수는 시작 숫자부터 이어간다.
출력
- 마지막 숫자부터 역순으로 숫자를 출력한다.
- 10개 이상인 경우 10개만 출력

풀이
- 마지막에서 처음으로 돌아오는 경우가 있기 때문에 원형리스트로 만든다.
- K번 반복하며 M씩 이동하여 앞, 뒤 노드의 데이터 값을 더한 데이터를 추가한다.
- 마지막으로 출력
"""

# 기본 연결 리스트 클래스 선언
class Node:
    def __init__(self, data):
        self.data = data    # 데이터 저장
        self.next = None    # 다음 노드 주소 저장


T = int(input())
for case in range(T):
    N, M, K = map(int, input().split()) # N: 숫자 N개, M: 추가할 칸, K: 반복횟수
    input_data = list(map(int, input().split()))  # 첫 입력 받기

    # 1. 원형 연결 리스트 만들기
    head = Node(input_data[0])
    current = head
    for i in range(1, N):
        new_node = Node(input_data[i])          # new_node 생성
        current.next = new_node                 # 현재노드의 다음 노드를 new_node로 연결
        current = new_node                      # 현재를 new_node로 변경
    current.next = head                 # 원형 리스트로 만들기 위해 다시 head와 연결
    
    # 2. K번 만큼 M씩 이동하며 값 추가
    current = head
    for j in range(K):
        for _ in range(M-1):
            current = current.next  # M-1번 만큼 이동해서 새로운 칸 이전을 current로
        new_data = current.data + current.next.data # 새로 넣을 값 = 현재 data + 다음 data
        new_node = Node(new_data)   # 새로 생성
        temp = current.next         # 현재 다음을 저장해놓고
        current.next = new_node     # 현재 다음을 new_node로 변경
        new_node.next = temp        # new_node의 다음은 원래 현재값의 다음으로 저장
        current = new_node          # current 값 업데이트
    
    # 3. 출력하기
    my_stack = []   # 원형 리스트니까 출력을 위해서 스택에 값들 저장
    current = head
    for c in range(N+K):
        my_stack.append(current.data)
        current = current.next
    
    print(f'#{case+1}', end=' ')
    if N + K >= 10:
        for _ in range(10):
            print(my_stack.pop(), end=' ')
    else:
        while my_stack:
            print(my_stack.pop(), end=' ')
    print()

