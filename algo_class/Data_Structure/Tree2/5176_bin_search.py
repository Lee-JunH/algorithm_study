"""
SWEA_5176 - 이진탐색 - D2

문제
- N까지의 자연수를 이진 탐색 트리에 저장하려 한다.
- 왼쪽 루트 < 현재 노드 < 오른족 루트를 만족하도록 트리를 만들어라.

출력
- 루트에 저장된 값과, N/2번 노드에 저장된 값을 출력

풀이
- 맨 왼쪽 아래부터 값을 넣어가는 과정인 중위순회를 실시한다.
"""


def inorder(cur):
    global data

    left = cur * 2
    right = cur * 2 + 1
    if cur > N:
        return
    inorder(left)
    tree[cur] = data
    data += 1
    if cur > N:
        return
    inorder(right)


T = int(input())
for case in range(T):
    N = int(input())
    tree = [0] * (N + 1)
    data = 1
    inorder(1)
    print(f'#{case+1} {tree[1]} {tree[N//2]}')

