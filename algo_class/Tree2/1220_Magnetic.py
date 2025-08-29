"""
SWEA_1220 - Magnetic - D3

문제
- 자성체들이 놓여 있다. 자기장을 걸었을 때, 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
- N극은 1, S극은 2
- 위쪽이 N극, 아래쪽이 S극

풀이
- 경우의 수
- N극
    - 밑으로 이동한다.
    - 예외
        - 밑에 S극이 있는 경우는 못내려간다.
        - N극
"""


T = 10
for case in range(T):
    B = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(B)]

    cnt = 0
    N = 0
    for i in range(B):
        for j in range(B):
            if magnetic[j][i] == 1:
                N = 1
            elif magnetic[j][i] == 2:
                if N == 1:
                    cnt += 1

