"""
SWEA_4875 - 미로 - D2

문제 설명
- NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는 지 확인하는 프로그램
"""

T = int(input())
for case in range(T):
    N = int(input())
    miro = list(map(int,input().split()))
    print (miro)