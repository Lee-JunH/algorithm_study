# SWEA_23795 - 우주괴물 - D1

T = int(input())
for case in range(T):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]

    blank = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] == 2:
                r = i
                c = j
            if space[i][j] == 0:
                blank += 1

    count = 0
    for k in range(N):
        if k < c:
            count += 1
            if space[r][k] == 1:
                count = 0
        elif k > c:
            if space[r][k] == 1:
                break
            count += 1
    count2 = 0
    for k in range(N):
        if k < r:
            count2 += 1
            if space[k][c] == 1:
                count2 = 0
        elif k > r:
            if space[k][c] == 1:
                break
            count2 += 1
    print(f'#{case+1} {blank - count - count2}')