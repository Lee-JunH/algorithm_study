"""
SWEA_1226 - 미로1 - D4

문제
- 16x16 미로에서 흰색은 길, 노란색은 벽이다.
- 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.
- 미로의 시작점은 (1,1)이고 도착점은 (13,13)이다.
- 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하라

출력
- 도달 가능 여부를 가능하면 1 불가능하면 0

풀이
- 큐를 이용한 BFS를 이용한다.
"""

from collections import deque

def bfs():
    while my_q:
        cur = my_q.popleft()
        for dir in range(4):
            nr = cur[0] + dr[dir]
            nc = cur[1] + dc[dir]
            if maze[nr][nc] == 1 or visited[nr][nc] == 1:
                continue
            if maze[nr][nc] == 3:
                return 1
            visited[nr][nc] = 1
            my_q.append([nr, nc])
    return 0

T = 10
for _ in range(T):
    case = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    visited = [[0 for _ in range(16)] for _ in range(16)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    my_q = deque()
    start = [1,1]
    visited[1][1] = 1
    my_q.append(start)
    print(f'#{case} {bfs()}')