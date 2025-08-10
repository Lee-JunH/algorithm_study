"""
SWEA_5105 - 미로의 거리 - D3

문제 설명
- NxN 미로에서 출발지와 목적지가 주어진다.
- 이 때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 계산하라
출력
- 경로가 있는 경우 최소 칸수
- 경로가 없는 경우 0
풀이
- 큐를 이용해 첫 번째 값을 pop하며 다음 칸으로 이동하여 출구를 찾는다.
"""


def backtrack(miro, N, queue, visited, count):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    global optimal

    while queue:
        row, col = queue.pop(0)     # queue에 저장된 첫 번째 값
        for dir in range(4):
            nr = row + dr[dir]
            nc = col + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue    # 인덱스 초과 확인
            if visited[nr][nc] == 1 or miro[nr][nc] == '1':
                continue    # 벽인지 방문한 곳인지 확인
            if miro[nr][nc] == '3':     # 도착지점인 경우
                if optimal > count:     # 제일 count가 적은 값 저장
                    optimal = count
                    break
            visited[nr][nc] = 1     # 방문 체크
            queue.append((nr, nc))      # 다음으로 이동하기 위해 다시 queue에 push
            backtrack(miro, N, queue, visited, count+1) # 이동한 곳에서 또 이동


T = int(input())
for case in range(T):
    N = int(input())
    miro = [list(input().strip()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    my_queue = []

    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                my_queue = [(i, j)]
                visited[i][j] = 1
                break

    optimal = 10000 # 최대 이동 횟수를 미리 지정
    backtrack(miro, N, my_queue, visited, 0)
    if optimal == 10000:    # 업데이트가 안된 경우 경로가 없으니 0으로 초기화
        optimal = 0
    print(f'#{case+1} {optimal}')

