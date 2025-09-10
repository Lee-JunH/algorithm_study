"""
SWEA_11315 - 오목판정 - D3

문제
- NxN 크기의 판에서 가로, 세로, 대각선 중 하나의 방향으로 5개 이상 연속한 부분 여부를 구하라
- 'o'는 돌이 있는 칸, '.'은 돌이 없는 칸을 의미

출력
- 5개 이상 연속한 부분이 있으면 'YES'
- 없으면 'NO'

풀이
- 가로, 세로, 크로스 확인 함수를 만든다.
"""

def check_g_s():
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if omoc[i][j] == 'o':
                cnt1 += 1
            else:
                if cnt1 >= 5:
                    return 'YES'
                cnt1 = 0
            if omoc[j][i] == 'o':
                cnt2 += 1
            else:
                if cnt2 >= 5:
                    return 'YES'
                cnt2 = 0
        if cnt1 >= 5 or cnt2 >= 5:
            return 'YES'
    return 'NO'

def cross():
    
    for i in range(N):
        for j in range(N):
            k = 0
            cnt1 = 0
            while 0 <= i+k < N and 0 <= j+k < N:
                if omoc[i+k][j+k] == 'o':
                    cnt1 += 1
                else:
                    if cnt1 == 5:
                        return 'YES'
                    cnt1 = 0
                k += 1
            if cnt1 >= 5:
                return 'YES'
            
            k = 0
            cnt2 = 0
            while 0 <= i+k < N and 0 <= j-k < N:
                if omoc[i+k][j-k] == 'o':
                    cnt2 += 1
                else:
                    if cnt2 == 5:
                        return 'YES'
                    cnt2 = 0
                k += 1
            if cnt2 >= 5:
                return 'YES'
    return 'NO'

T = int(input())
for case in range(T):
    N = int(input())
    omoc = [input() for _ in range(N)]

    result = check_g_s()
    if result == 'NO':
        result = cross()
    print(f'#{case+1} {result}')