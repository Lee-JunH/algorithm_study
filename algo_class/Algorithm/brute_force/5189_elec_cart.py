"""
SWEA_5189 - 전자카트 - D3

문제
- 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
- 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하라
"""

def dfs(r, hap, cnt):
    global min_b

    if cnt == N:
        if min_b > hap+battery[r][0]:
            min_b = hap+battery[r][0]
        return
    if hap > min_b:
        return
    
    for i in range(1, N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        dfs(i, hap+battery[r][i], cnt+1)
        visited[i] = 0
    

T = int(input())
for case in range(T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    min_b = 1001
    visited = [0 for _ in range(N)]
    dfs(0,0,1)

    print(f'#{case+1} {min_b}')