"""
SWEA_2001 - 파리 퇴치 - D2

문제 설명
NXN 배열 안에 있는 파리를 MXM의 파리채로 죽일 때 가장 많이 죽일 수 있는 경우를 출력
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    fly_lst = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_fly = 0
            for col in range(i, i+M):
                for row in range(j, j+M):
                    sum_fly += fly_lst[col][row]
            if sum_fly > max_fly:
                max_fly = sum_fly
    print(f'#{case+1} {max_fly}')

