"""
SWEA_1251 - 하나로 - D4

문제
- 모든 섬을 해저터널로 연결하는 것이 목표이다
- 해저 터널은 반드시 두 섬을 선분으로 연결하며
- 두 해저 터널이 교차된다 하더라도 물리적으로는 연결되지 않는 것으로 가정한다.
- 환경 부담금 정책
    - 환경 부담 세율(E)과 해저터널 길이(L)의 제곱의 곱(E*L^2)만큼 지불
- 총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결할 수 있는 교통시스템 설계
"""

def find_set(x):    # 부모 찾기
    if x == parent[x]:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):     # x, y 합치기
    rx = find_set(x)    # x의 부모값
    ry = find_set(y)    # y의 부모값

    if rx == ry:        # 같은 자식인 경우 리턴
        return
    
    parent[ry] = rx     # ry의 부모를 rx로 변경

T = int(input())
for case in range(T):
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    tax = float(input())

    # i -> j로 가는 비용 계산해 놓기
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            cost = ((x_lst[i] - x_lst[j]) ** 2 + ((y_lst[i] - y_lst[j]) ** 2)) * tax
            edges.append((i,j,cost))

    # 비용에 따라 정렬
    edges.sort(key=lambda x:x[2])

    parent = [i for i in range(N)]
    cnt = 0
    min_cost = 0
    for u,v,w in edges:
        if find_set(u) != find_set(v):       # u와 v가 같은 집합인지 확인
            union(u, v)
            min_cost += w
            cnt += 1
        
        if cnt == N-1:
            break
    
    print(f'#{case+1} {min_cost:.0f}')