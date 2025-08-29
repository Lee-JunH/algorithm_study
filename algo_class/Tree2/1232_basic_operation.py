"""
SWEA_1232 - 사칙연산 - D4

문제
- 사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다.
- 임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 결과와 오른쪽 결과에 해당 연산자를 적용
    - 입력
        - 정점이 정수 : 정점번호, 양의 정수
        - 정점이 연산자 : 정점 번호, 연산자, 왼쪽 자식, 오른쪽 자식
출력
- 계산한 결과를 출력

풀이
- 먼저 값을 트리에 저장해 놓고 뒤에서 부터 순회한다.
- 연산자를 만나면 왼쪽 오른쪽 값을 확인하여 연산한다.
"""


def operation(cur):
    if tree[cur][0] in '-+/*':
        left = operation(int(tree[cur][1]))
        right = operation(int(tree[cur][2]))
        if tree[cur][0] == '-':
            tree[cur][0] = left - right
        elif tree[cur][0] == '+':
            tree[cur][0] = left + right
        elif tree[cur][0] == '*':
            tree[cur][0] = left * right
        elif tree[cur][0] == '/':
            tree[cur][0] = left / right
    return int(tree[cur][0])


T = 10
for case in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        lst = list(input().split())
        tree[int(lst[0])] = lst[1:]
    print(f'#{case+1} {operation(1)}')





