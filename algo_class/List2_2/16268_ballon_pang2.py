"""
SWEA_16268 - 풍선팡2 - D2

문제 설명
풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터진다
꽃가루 개수 A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 중 최대값을 출력하라
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    ballon = [list(map(int, input().split())) for _ in range(N)]

    max_b = 0
    for i in range(N):
        for j in range(M):
            sum_b = ballon[i][j]
            for dir_r, dir_c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nr = i + dir_r
                nc = j + dir_c
                if nr < 0 or nr >= N or nc < 0 or nc >= M:
                    continue
                sum_b += ballon[nr][nc]
            if max_b < sum_b:
                max_b = sum_b
    print(f'#{case+1} {max_b}')


