"""
SWEA_5188 - 최소합 - D3

문제
- NxN 칸에서 오르쪽이나 아래로만 이동할 수 있다.
- 맨 왼쪽 위에서 오른족 아래까지 이동할 때, 지나간 칸의 숫자 합이 최소가 되도록 하라.
"""

def dfs(r, c, hap):
    global min_hap

    if r == N-1 and c == N-1:   # 최종 위치로 오면 min값 업데이트
        if min_hap > hap:
            min_hap = hap
        return
    if hap > min_hap:   # 이미 너무 크면 돌아가
        return
    
    if c+1 < N:
        dfs(r, c+1, hap+board[r][c+1])    # 오른쪽으로 이동

    if r+1 < N:
        dfs(r+1, c, hap+board[r+1][c])    # 아래로 이동

T = int(input())
for case in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_hap = 13 * 10 * 2

    dfs(0, 0, board[0][0])    # 현재 위치 (0,0), 현재 합

    print(f'#{case+1} {min_hap}')