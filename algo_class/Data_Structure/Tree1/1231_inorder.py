"""
SWEA_1231 - 중위순회 - D4

문제
- 중위순회하여 노드에 저장된 단어를 출력해라.

풀이
- 중위순회하기
"""

def inorder(n):
    left = n * 2
    right = n * 2 + 1

    if left <= N:
        inorder(left)
    print(node[n-1][1], end='')
    if right <= N:
        inorder(right)

T = 10
for case in range(T):
    N = int(input())
    node = [list(input().split()) for _ in range(N)]

    print(f'#{case+1}', end=' ')
    inorder(1)
    print()
    