"""
SWEA_1865 - 동철이의 일 분배 - D4

문제
- N명의 직원에게 공평하게 일을 하나씩 배분하려고 한다.
- 해야할 일에도 번호가 N까지 있고, i번 직원이 j번 일을 하면 성공할 확률이 주어진다.
- 주어진 일을 모두 성공할 확률의 최댓값을 구하는 문제
"""

def backtrack(staff, P):
    global p_complete

    if P * 100 < p_complete:        # 이게 가장 중요 (가지치기)
        return

    if staff == N:  # 마지막까지 내려왔을 때
        P *= 100
        p_complete = max(p_complete, P)
        return

    for i in range(N):
        if not complete[i]:
            my_p = work[staff][i]
            if my_p == 0:
                continue
            complete[i] = 1
            backtrack(staff+1, P * (my_p / 100))
            complete[i] = 0
    
T = int(input())
for case in range(T):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]

    complete = [0] * N
    p_complete = 1
    backtrack(0, 1)
    print(f'#{case+1} {p_complete:.6f}')