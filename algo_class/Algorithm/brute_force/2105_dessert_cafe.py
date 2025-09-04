"""
SWEA_2105 - 디저트 카페 - 모의 SW 역량테스트

문제
- 한 변의 길이가 N인 정사각형 모양을 가진 지역에 각 칸에는 디저트의 종류 수가 적혀있다.
- 카페들 사이에는 대각선 방향으로 움직일 수 있다.
- 어느 한 카페에서 출발하여 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
- 같은 숫자의 디저트를 파는 곳에 있으면 안된다.

출력
- 디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 출력
- 디저트를 먹을 수 없는 경우 -1

풀이
- 처음부터 끝까지 모두 탐색해보자
- 처음엔 1번씩만 대각으로 이동하고 두번재 탐색부터 두칸씩 가자
- 회전 방향은 이전 방향과 같거나 
"""

def dfs(r, c):
    global max_d

    if my_dessert[dessert[r][c]] == 1:
        return
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr < 0 or nr >= N or nc < 0 or nr >= N:
            continue
        my_dessert[dessert[r][c]] = 1

        dfs(r+dr[i], c+dc[i])


T = int(input())
for case in range(T):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]
    max_d = 0
    vis = [[0 for _ in range(N)] for _ in range(N)]
    my_dessert = [0 for _ in range(101)]

    dfs()

    print(f'#{case+1} {max_d}')