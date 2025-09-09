"""
SWEA_5656 - 벽돌 깨기 - 모의 SW 역량테스트

문제
- 구슬을 N번 쏴서 WxH에 있는 벽돌을 깨려고 한다.
- N개의 벽돌을 떨어뜨려 남은 벽돌의 개수를 구하라.

조건
- 구슬은 좌, 우로만 움직이고 항상 맨 위에 있는 벽돌만 깰 수 있다.
- 구슬이 맞춘 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1)칸 만큼 제거 된다.
- 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
- 빈공간이 있으면 벽돌은 밑으로 떨어진다.

풀이
1. 깰 벽돌 정하기
    - 맨 위의 벽돌만 깰 수 있으니까 총 W * N만큼 반복해야한다.
    - W개의 벽돌에서 하나랑 정하고 또 정리된 벽돌 W개의 벽돌에서 깨고... 이걸 N번 반복
2. 벽돌 깨기
    - 어떠한 지점 부터 일단 벽돌숫자만큼 깬다.
    - 1보다 작은 수를 만나면 멈추고
    - 1보다 큰 수를 만나면 스택에 넣어 놓고 그거에 대해서 또 깬다.
3. 깨고난 후 벽돌 아래로 내리기
3-1. 깨고 벽돌을 내리는 방법도 있지만 아니면 0을 만나면 숫자를 만날 때 까지 더 진행해 보는 것도 괜찮을 듯
"""

def left_brick():       # 남은 벽돌 세는 함수
    cnt = 0

    for i in range(H):
        for j in range(W):
            if brick[i][j] != 0:
                cnt += 1
    return cnt

def restore_brick():    # 부순 벽돌 복구 함수
    pass

def destroy_brick(r, c, t_brick):    # 벽돌 부수는 함수
    b_stack = [(r, c)]

    while b_stack:
        x, y = b_stack.pop()
        temp = brick[x][y] - 1
        for i in range(r-temp, r+temp+1):   # r 주위
            for j in range(c-temp, c+temp+1):   # c 주위
                if brick[i][j] != 0:    # 0이 아니면
                    t_brick[i][j] = brick[i][j]     # 지우기
                    if brick[i][j] >= 2:
                        b_stack.append((i,j))
                    brick[i][j] = 0


def select_brick(b_brick):  # 벽돌 선택 함수
    global min_brick

    if b_brick == N:
        min_brick = min(min_brick, left_brick())
        return

    for j in range(H):
        temp_brick = [[0 for _ in range(W)] for _ in range(H)]
        for i in range(W):
            if brick[i][j] != 0:
                destroy_brick(i, j, temp_brick)
                select_brick(b_brick + 1)
                restore_brick(temp_brick)
                break

T = int(input())
for case in range(T):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]

    min_brick = W * H
    select_brick(0)

    print(f'#{case+1} {min_brick}')