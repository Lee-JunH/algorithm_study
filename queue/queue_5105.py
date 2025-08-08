"""
SWEA_5105 - 미로의 거리 - D3

문제 설명
- NxN 미로에서 출발지와 목적지가 주어진다.
- 이 때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 계산하라
출력
- 경로가 있는 경우 최소 칸수
- 경로가 없는 경우 0
"""


def backtrack(miro, N):
    count = 0

    return count


T = int(input())
for case in range(T):
    N = int(input())
    miro = [list(map(int, input().split())) for _ in range(N)]

    optimal = backtrack(miro, N)
    print(f'#{case+1} {optimal}')

