# SWEA_20397 - 돌 뒤집기 게임2 - D1

T = int(input())
for case in range(T):
    N, M = int(input())     # N : 돌의 수, M : 뒤집기 횟수
    stone = list(input().split())

    for _ in range(M):
        i, j = map(int, input().split())

        

