"""
SWEA_5177 - 이진 힙 - D2

문제
- 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
- 부모 노드의 값 < 자식 노드의 값을 유지한다.
- N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고,
- 마지막 노드의 조상 노드에 저장된 정수의 합을 구하라

출력
- 마지막 노드의 조상 노드에 저장된 정수의 합

풀이
- 부모노드의 값과 비교를 할텐데 자식노드의 //2 가 부모노드인 것을 이용할 수 있을까?
- 비교 후 바뀐 값에 대해 비교를 반복해야 함
""" 

def heap_in(node, cur):

    heap[cur] = node   # 힙에 먼저 입력

    child = cur         # 자신
    parent = cur // 2   # 부모노드

    while child > 1:
        if heap[child] < heap[parent]:
            heap[parent], heap[child] = heap[child], heap[parent]
        child = parent      # 자신의 위치를 부모 노드로
        parent = child // 2 # 부모노드는 자신의 위치 // 2

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    # 1.힙에 입력하기
    heap = [0] * (N+1)      # heap 선언
    cur = 1
    for node in lst:
        heap_in(node, cur)  # 하나씩 힙에 입력
        cur += 1
    
    # 2.출력하기
    result = 0
    while N > 0:
        N //= 2
        result += heap[N]
    print(f'#{case+1} {result}')