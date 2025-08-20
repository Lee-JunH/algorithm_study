"""
SWEA_5097 - 회전 - D2

문제
- N개의 숫자로 이루어진 수열이 주어진다.
- 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞의 숫자 출력

풀이
- 큐로 직접 구현하는 것도 가능하지만, N과 M의 연산으로 최소 횟수 구할 수 있음
"""

from collections import deque

T = int(input())
for case in range(T):
    N, M = map(int, input().split())

    my_q = deque()
    my_q.extend(list(map(int, input().split())))

    rotate = M % N
    for _ in range(rotate):
        my_q.append(my_q.popleft())
    print(f'#{case+1} {my_q.popleft()}')