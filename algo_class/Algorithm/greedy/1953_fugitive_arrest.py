"""
SWEA_1953 - 탈주범 검거 - 모의 SW 역량테스트

문제
- 탈주범이 한시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔다.
- 시간당 1의 거리를 움직일 수 있다.

풀이
- bfs로 한칸씩 뻗어가면서 visited 를 업데이트 하고 visit한 장소 수를 세면 되지 않을까?
- 방향만 새로 설정해주자.
"""

def tunnel(t):
    direction = []
    if t == 1:
        direction = [(-1, 0, 'up'), (0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l')]
    elif t == 2:
        direction = [(-1, 0, 'up'), (1, 0, 'd')]
    elif t == 3:
        direction = [(0, 1, 'r'), (0, -1, 'l')]
    elif t == 4:
        direction = [(-1, 0, 'up'), (0, 1, 'r')]
    elif t == 5:
        direction = [(1, 0, 'd'), (0, 1, 'r')]
    elif t == 6:
        direction = [(1, 0, 'd'), (0, -1, 'l')]
    elif t == 7:
        direction = [(-1, 0, 'up'), (0, -1, 'l')]
    return direction

def connected(dir1, dir2):
    if dir1 == 'up':
        if dir2 == 3 or dir2 == 4 or dir2 == 7:
            return 0
    if dir1 == 'd':
        if dir2 == 3 or dir2 == 5 or dir2 == 6:
            return 0
    if dir1 == 'r':
        if dir2 == 2 or dir2 == 4 or dir2 == 5:
            return 0
    if dir1 == 'l':
        if dir2 == 2 or dir2 == 6 or dir2 == 7:
            return 0
    return 1

def bfs(vis):
    global cnt

    my_q = deque()
    my_q.append((R, C)) # 초기 위치 입력

    while my_q:
        r, c = my_q.popleft()
        if vis[r][c] == L:
            return
        for dr, dc, direct in tunnel(my_map[r][c]):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M:      # 범위를 벗어나는 경우
                continue
            if vis[nr][nc] >= 1 or my_map[nr][nc] == 0:    # 방문 했거나, 터널이 없는 경우
                continue
            if not connected(direct, my_map[nr][nc]):
                continue
            vis[nr][nc] = vis[r][c] + 1
            my_q.append((nr, nc))
            cnt += 1

from collections import deque
 
T = int(input())
for case in range(T):
    N, M, R, C, L = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1
    cnt = 1
    bfs(visited)
    print(f'#{case+1} {cnt}')