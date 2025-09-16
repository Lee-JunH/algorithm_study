"""
SWEA_5247 - 연산 - D4

문제
- 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만드려고 한다.
- +1, -1, *2, -10 네가지라고 할 때, 최소 몇 번의 연산을 거쳐야 하는지 알아내는 문제
- 단, 연산 중간 결과도 항상 백만 이하의 자연수여야 한다.
"""

def bfs(num, cnt):
    global min_cnt

    
T = int(input())
for case in range(T):
    N, M = map(int, input().split())

    min_cnt = float('inf')
    bfs(N, 0)

    print(f'#{case+1} {min_cnt}')