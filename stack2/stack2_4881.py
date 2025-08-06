"""
SWEA_4881 - 배열 최소 합 - D2

문제 설명
> NxN 배열에서 한 줄에 하나씩 골라 합이 최소가 되도록 한다.
> 단, 세로로 같은 줄에서 2개 이상의 숫자를 고를 수 없다.
"""

T = int(input())
for case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    