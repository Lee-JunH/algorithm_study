"""
SWEA_1215 - 회문1 - D3

문제
- 8x8 글자판에서 길이가 5인 회문의 개수를 반환하라

풀이
- 
"""

T = 10
for case in range(T):
    N = int(input())
    pd = [list(input().strip()) for _ in range(8)]

    count = 0
    for i in range(8):
        for j in range(8-N+1):
            temp1 = pd[i][j:j+N]
            temp2 = pd[i][j+N-1:j:-1]
            temp2.append(pd[i][j])
            if temp1 == temp2:
                count += 1
    pd_r = list(zip(*pd))
    for i in range(8):
        for j in range(8-N+1):
            temp1 = list(pd_r[i][j:j+N])
            temp2 = list(pd_r[i][j+N-1:j:-1])
            temp2.append(pd_r[i][j])
            if temp1 == temp2:
                count += 1
    print(f'#{case+1} {count}')