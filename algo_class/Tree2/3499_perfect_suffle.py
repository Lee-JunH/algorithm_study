"""
SWEA_3499 - 퍼펙트 셔플 - D3

문제
- A~ 카드를 퍼펙트 셔플 한다는 것은 카드 덱을 정확히 절반으로 나누고 나누 것들에서
- 교대로 카드를 뽑아 새로운 덱을 만드는 것이다.
- N이 홀수면 교대로 놓을 때 먼저 놓는 쪽에 한장이 더 들어가게 한다.

출력
- 퍼펙트 셔플 후의 카드 순서를 출력

풀이
- 인덱싱을 이용하여 2개의 리스트로 나누고 하나씩 출력한다.
"""

from collections import deque

T = int(input())
for case in range(T):
    N = int(input())
    card = list(input().split())

    if N % 2 == 0:
        first = deque(card[:N//2].copy())
        second = deque(card[N//2:].copy())
    else:
        first = deque(card[:N//2 + 1].copy())
        second = deque(card[N//2 + 1:].copy())
    j = 0
    print(f'#{case+1} ',end='')
    while True:
        if not first:
            break
        print(first.popleft(), end=' ')
        if not second:
            break
        print(second.popleft(), end=' ')
    print()
