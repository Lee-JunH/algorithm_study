"""
SWEA_4861 - 회문 - D2

문제
- NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하라

** 회문은 1개가 존재
** 가로, 세로 모두 체크

풀이
- 
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    pd = [list(input().strip()) for _ in range(N)]

    find = 0
    for i in range(N):
        for j in range(N-M+1):
            temp1 = pd[i][j:j+M]
            temp2 = temp1[::-1]
            if temp1 == temp2:
                find = 1
                break
        if find == 1:
            break
    if find == 0:
        pd_r = list(zip(*pd))
        for i in range(N):
            for j in range(N-M+1):
                temp1 = list(pd_r[i][j:j+M])
                temp2 = temp1[::-1]
                if temp1 == temp2:
                    find = 1
                    break
            if find == 1:
                break
    print(f'#{case+1}', end=' ')
    for num in temp1:
        print(num, end='')
    print()