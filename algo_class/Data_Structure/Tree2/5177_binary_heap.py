"""
SWEA_18526 - 이진 힙 - D2

문제
- 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 구하라.
- 최소힙
    - 부모 노드의 값 < 자식 노드의 값 
    - 이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.

풀이
- 값을 넣고 부모노드로 계속 올라가며 비교 및 교환한다.
"""

T = int(input())
for case in range(T):
    N = int(input())
    node = list(map(int, input().split()))
    tree = [0] * (N+1)
    j = 0
    for i in range(1, N+1):
        tree[i] = node[j]
        j += 1
        temp = i
        while temp // 2 >= 1:
            if tree[temp] < tree[temp // 2]:
                tree[temp], tree[temp//2] = tree[temp//2], tree[temp]
            temp //= 2
    hap = 0
    while N != 0:
        N //= 2
        hap += tree[N]
    print(f'#{case+1} {hap}')