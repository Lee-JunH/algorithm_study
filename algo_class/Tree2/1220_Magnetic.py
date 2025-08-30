"""
SWEA_1220 - Magnetic - D3

문제
- 자성체들이 놓여 있다. 자기장을 걸었을 때, 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
- N극은 1, S극은 2
- 위쪽이 N극, 아래쪽이 S극

풀이
- 한 열씩만 확인하면 된다.
- N극을 만났을 때가 중요하다
    - N극을 만나면 stack에 입력해 놓고
    - S극을 만나면
"""

T = 10
for case in range(T):
    B = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(B)]

    cnt = 0
    for i in range(B):
        N = 0
        for j in range(B):
            if magnetic[j][i] == 1: # N극일 때
                N = 1
            elif magnetic[j][i] == 2:   # S극일 때
                if N == 1:
                    cnt += 1
                    N = 0
    print(f'#{case+1} {cnt}')

