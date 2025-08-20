"""
SWEA_5174 - subtree - D2

문제
- 트리의 일부를 서브트리라고 한다.
- 주어진 이진 트리에서 노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아내시오

출력
- 서브트리의 노드 개수

풀이
- 딕셔너리로 값들을 연결하고 스택에 넣으면서 dfs를 진행해 계산하기
"""


def dfs():
    global cnt
    
    cnt += 1
    while my_queue:
        temp = my_queue.pop()
        if temp in my_dict:
            for num in my_dict[temp]:
                my_queue.append(num)
                dfs()


T = int(input())
for case in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    my_dict = {}
    for i in range(0, E*2, 2):
        my_dict.setdefault(lst[i], [])
        my_dict[lst[i]].append(lst[i+1])
    
    my_queue = []
    cnt = 0
    my_queue.append(N)
    dfs()
    print(f'#{case+1} {cnt}')