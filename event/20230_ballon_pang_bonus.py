# SWEA_20230 - 풍선팡 보너스게임2 - D2

T = int(input())
for case in range(T):
    N = int(input())
    ballon = [list(map(int, input().split())) for _ in range(N)]

    sum_b = 0
    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum_b = -ballon[i][j]
            for k in range(N):
                sum_b += ballon[i][k] + ballon[k][j]
                if max_sum < sum_b:
                    max_sum = sum_b
    print(f'#{case+1} {max_sum}')