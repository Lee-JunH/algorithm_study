"""
SWEA_5110 - 수열 합치기 - D3

문제
- 여러 개의 수열을 아래의 규칙에 따라 합친다.
    - 수열2의 첫 숫자보다 큰 숫자를 수열1에서 찾아 그 앞에 끼워 넣는다.
    - 큰 숫자가 없는 경우 맨 뒤에 붙인다.

출력
- 마지막 수열까지 합치고, 맨 뒤의 숫자부터 역순으로 10개 출력

풀이
- 앞 문제와 같이 찾은 숫자의 인덱스에 새로운 리스트 추가해준다.
- 위 방법으로 안풀려서 연결 리스트를 만들어서 풀자.
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())    # N: 수열의 길이, M: 수열의 개수

    result = [1001]
    for i in range(M):
        suyeol = list(map(int, input().split()))    # 하나씩 받아서 확인하기
        for j in range(N * i + 1):  # 처음엔 바로 입력하기 위한 범위
            if suyeol[0] < result[j]:   # 첫번째 값보다 크면 입력
                result[j:j] = suyeol    # 리스트를 합치는 법 [i:i] 활용
                break
    result = result[N*M-1::-1]
    print(f'#{case+1}', end=' ')
    for k in range(10):
        print(result[k], end=' ')
    print()

# # 연결리스트 클래스 선언하는 법
# class Node:
#     def __init__(self, data):
#         self.prev = None
#         self.data = data
#         self.next = None

# def link_insert(su, head):
#     index = 0
#     cur = head
#     while cur.next:
#         if cur.data > su[0]:    # 추가할 위치로 이동
#             break
#         cur = cur.next
#     if cur.next != None:
#         cur = cur.prev
#     temp = cur.next     # cur의 다음 값 임시 저장
#     for i in range(N):
#         new_node = Node(suyeol[i])   # new_node를 data로 생성
#         cur.next = new_node     # cur의 다음 주소를 new_node로 변경
#         new_node.prev = cur     # new_node의 이전 값은 cur 값
#         cur = new_node
#     new_node.next = temp
#     temp.prev = new_node

# T = int(input())
# for case in range(T):
#     N, M = map(int, input().split())    # N: 수열의 길이, M: 수열의 개수
    
#     head = None
#     for i in range(M):
#         suyeol = list(map(int, input().split()))
#         if i == 0:
#             head = Node(suyeol[0])
#             cur = head
#             for data in range(1, N):
#                 new_node = Node(suyeol[data])
#                 new_node.prev = cur
#                 cur.next = new_node
#                 cur = new_node
#         else:
#             link_insert(suyeol, head)
    
#     cur = head
#     while cur:  # 마지막까지 이동
#         cur = cur.next
#     print(f'#{case+1}', end=' ')
#     for _ in range(10):
#         print(cur.data, end=' ')
#         cur = cur.prev  # 이전으로 이동
#     print()
