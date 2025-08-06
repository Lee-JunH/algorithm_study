"""
SWEA_4836 - 색칠하기 -D2

문제 설명
N개의 영역에서 왼쪽 위, 오른쪽 아래 모서리 인덱스가 주어질 때 색이 겹쳐 보라색인 칸 수를 구하라
"""

T = int(input())
for case in range(T):
    N = int(input())

    count = 0
    board = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                board[i][j] += color
                if board[i][j] == 3:
                    count += 1
    print(f'#{case+1} {count}')

