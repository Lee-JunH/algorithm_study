# SWEA_20397 - 돌 뒤집기 게임2 - D1

T = int(input())
for case in range(T):
    N, M = map(int, input().split())     # N : 돌의 수, M : 뒤집기 횟수
    stone = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            if i-1-k >= 0 and i-1+k < N:
                if stone[i-1+k] == stone[i-1-k]:
                    if stone[i-1+k] == 1:
                        stone[i-1+k] = 0
                        stone[i-1-k] = 0
                    else:
                        stone[i-1+k] = 1
                        stone[i-1-k] = 1
            else:
                break
    print(f'#{case+1} ', end='')
    for n in stone:
        print(n, end=' ')
    print()