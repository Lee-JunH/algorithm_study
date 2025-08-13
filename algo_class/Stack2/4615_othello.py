"""
SWEA_4615 - 재미있는 오셀로 게임 - D3

문제
- 오셀로는 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서
- 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
- 보드는 4x4, 6x6, 8x8 크기를 사용한다.
- 조건
    - 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있음
    - 그 때의 상대편의 돌은 자신의 돌로 만들 수 있음

출력
- 보드에 있는 흑돌, 백돌의 개수를 출력

풀이
- 
"""

def count_b_w(b):
    count_b = 0
    count_w = 0
    for i in range(N):
        for j in range(N):
            if b[i][j] == 1:
                count_b += 1
            elif b[i][j] == 2:
                count_w += 1
    return count_b, count_w

def valid(r, c, color):
    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if color != board[nr][nc] and board[nr][nc] != 0:
            return 1
    return 0

def othello(c,d,color, i, count):  # 현재 위치 a,b , 방향 i, 사이 돌 개수
    while True:
        nr = c + dr[i]
        nc = d + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            return 0
        if color != board[nr][nc] and board[nr][nc] != 0:
            count += 1
            c = nr
            d = nc
        elif board[nr][nc] == 0:
            return 0
        elif color == board[nr][nc]:
            return count


T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]    # 위부터 시계방향 8방향
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    board[N-(N//2)-1][N-(N//2)-1] = 2
    board[N-(N//2)][N-(N//2)] = 2
    board[N-(N//2)][N-(N//2)-1] = 1
    board[N-(N//2)-1][N-(N//2)] = 1

    for _ in range(M):
        b,a,color = map(int, input().split())
        b -= 1
        a -= 1
        if not valid(a,b,color):    # 놓을 수 없는 곳인지 확인
            continue        # 못놓으면 상대편 차례로 이동
        board[a][b] = color
        for i in range(8):
            r = othello(a, b, color, i, 0)
            for j in range(1, r + 1):
                nr = a + dr[i] * j
                nc = b + dc[i] * j
                board[nr][nc] = color
    black, white = count_b_w(board)
    print(f'#{case+1} {black} {white}')
