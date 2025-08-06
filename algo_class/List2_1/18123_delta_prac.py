"""
SWEA_18123 - 델타연습 - D1

문제 설명
5X5 2차원 배열에서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
"""

T = int(input())
for case in range(T):
    N = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    sum_num = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    continue
                sum_num += abs(num_lst[i][j] - num_lst[ny][nx])
    print(f'#{case+1} {sum_num}')

