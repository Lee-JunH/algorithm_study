"""
SWEA_5248 - 그룹 나누기 - D3

문제
- 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출한다.
- 한 조의 인원에 제한을 두지 않아씩 때문에, 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모드 같은 조가 된다.
- 전체 몇 개의 조가 만들어지는가
"""

def dfs(idx):
    for n in node[idx]:
        if not visit[n]:
            visit[n] = 1
            dfs(n)

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    jo = list(map(int, input().split()))

    node = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        node[jo[i]].append(jo[i+1])
        node[jo[i+1]].append(jo[i])

    visit = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visit[i]:
            visit[i] = 1
            dfs(i)
            cnt += 1
    print(f'#{case+1} {cnt}')