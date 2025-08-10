# SWEA_22375 - 스위치 조작 - D1

T = int(input())
for case in range(T):
    N = int(input())

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if end[i] != start[i]:
            count += 1
            for j in range(i+1, N):
                if start[j] == 1: start[j] = 0
                else: start[j] = 1
    print(f'#{case+1} {count}')

