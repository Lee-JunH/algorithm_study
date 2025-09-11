"""
SWEA_5208 - 전기버스2 - D3

문제
- 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
- 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 문제
- 출발지에서의 배터리 장착은 교환 횟수에서 제외

풀이
- battery 값을 갱신하면서 이동하는데 battery가 0이 되면 돌아오도록 해서 가지치기 한다.
"""

def backtrack(stop, battery, cnt):
    global cnt_change

    for i in range(stop + battery, stop, -1):   # 최대 갈 수 있는 곳 부터 탐색
        if i >= N:   # 도착할 수 있으면 교환 횟수 업데이트
            cnt_change = min(cnt_change, cnt)
            return
        if cnt + 1 >= cnt_change:
            continue
        backtrack(i, bus_stop[i], cnt+1)

T = int(input())
for case in range(T):
    bus_stop = list(map(int, input().split()))
    N = bus_stop[0]

    cnt_change = N
    backtrack(1, bus_stop[1], 0)

    print(f'#{case+1} {cnt_change}')