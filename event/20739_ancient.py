# SWEA_20739 - 고대 유적2 - D2

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    pixel = [list(map(int, input().split())) for _ in range(N)]

    max_count = []
    for i in range(N):
        count = 0
        for j in range(M):
            if pixel[i][j] == 1:
                count += 1
            else:
                if count > 1:
                    max_count.append(count)
                count = 0
        if count > 1:
            max_count.append(count)
    
    for c in range(M):
        count = 0
        for r in range(N):
            if pixel[r][c] == 1:
                count += 1
            else:
                if count > 1:
                    max_count.append(count)
                count = 0
        if count > 1:
            max_count.append(count)
    max_b = 0
    for b in max_count:
        if max_b < b:
            max_b = b
    print(f'#{case+1} {max_b}')
