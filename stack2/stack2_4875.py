"""
SWEA_4875 - 미로 - D2

문제 설명
- NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는 지 확인하는 프로그램
"""
T = int(input())
for case in range(T):
    N = int(input())
    miro = [list(map(int, input().strip())) for _ in range(N)]

    vis = [[0]*N for _ in range(N)]     # 출발 지점 찾기
    for i_y in range(N):
        for i_x in range(N):
            if miro[i_y][i_x] == 2:
                x_start = i_x
                y_start = i_y
                break
    
    my_stack = []
    dx = [0, 1, 0, -1]  # x축 방향 (up, right, down, left)
    dy = [-1, 0, 1, 0]  # y축 방향
    result = 0
    my_stack.append((x_start, y_start)) # 초기 위치 push
    vis[y_start][x_start] = 1   # 현재 위치 방문 확인

    while my_stack:
        x, y = my_stack.pop()
        for dir in range(4):      # 4방향 확인
            nx = x + dx[dir]      # 현재 위치에 x, y 방향 더해주기
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 위치가 인덱스를 넘어가는 경우 제외
                continue
            if vis[ny][nx] == 1 or miro[ny][nx] == 1:   # 이미 방문한 곳이거나 벽인 경우 제외
                continue
            if miro[ny][nx] == 3:
                result = 1
                break
            vis[ny][nx] = 1     # 현재 위치 방문 확인
            my_stack.append((nx,ny))    # 현재 위치 스택에 push
    print(f'#{case+1} {result}')

# 함수로 뺀 경우
# def back_tracking(N, miro, x_start, y_start):
#     my_stack = []
#     dx = [0, 1, 0, -1]  # x축 방향 (up, right, down, left)
#     dy = [-1, 0, 1, 0]  # y축 방향
#     my_stack.append((x_start, y_start)) # 초기 위치 push
#     vis[y_start][x_start] = 1   # 현재 위치 방문 확인

#     while my_stack:
#         x, y = my_stack.pop()
#         for dir in range(4):      # 4방향 확인
#             nx = x + dx[dir]      # 현재 위치에 x, y 방향 더해주기
#             ny = y + dy[dir]
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 위치가 인덱스를 넘어가는 경우 제외
#                 continue
#             if vis[ny][nx] == 1 or miro[ny][nx] == 1:   # 이미 방문한 곳이거나 벽인 경우 제외
#                 continue
#             if miro[ny][nx] == 3:
#                 return 1
#             vis[ny][nx] = 1     # 현재 위치 방문 확인
#             my_stack.append((nx,ny))    # 현재 위치 스택에 push
#     return 0