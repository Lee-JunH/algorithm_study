"""
SWEA_20397 - 돌 뒤집기 게임2 - D1

문제
- i번째 돌을 사이에 두고 마주보는 j개의 돌이 있다.
- 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.

풀이
- i를 기준으로 j만큼 이동한 돌이 같은지 확인한다.
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    stone = list(input().split())
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for k in range(1, j+1):
            if i+k >= N or i-k < 0:
                continue
            if stone[i+k] == stone[i-k]:
                if stone[i+k] == '1':
                    stone[i+k] = '0'
                    stone[i-k] = '0'
                else:
                    stone[i+k] = '1'
                    stone[i-k] = '1'
    print(f'#{case+1} {" ".join(stone)}')