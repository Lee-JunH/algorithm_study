"""
SWEA_1210 - Ladder1 - D4

문제 설명
100x100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하라
"""


def check_col(col, N):
    if col >= N or col < 0:
        return 0
    return 1


def ladder_tagi(col, lad, N):
    row = 0
    visited = [[0] * N for _ in range(N)]
    while row < N:
        if row == N-1:
            if lad[row][col] == 2:
                return 1
            else:
                return 0
        visited[row][col] = 1
        if check_col(col-1, N) == 1 and lad[row][col - 1] == 1 and visited[row][col - 1] == 0:
            col -= 1
        elif check_col(col+1, N) == 1 and lad[row][col + 1] == 1 and visited[row][col + 1] == 0:
            col += 1
        else:
            row += 1
    return 0


T = 10
for _ in range(T):
    N = 100
    case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        if ladder[0][i] == 1:
            if ladder_tagi(i, ladder, N) == 1:
                break
    print(f'#{case} {i}')

