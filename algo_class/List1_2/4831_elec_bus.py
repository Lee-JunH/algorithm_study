"""
SWEA_4831 - 전기버스 - D3

문제 설명
- 전기버스는 한번 충전으로 K개의 정류장을 이동할 수 있다.
- M개의 충전기가 설치된 경로에서 최소 충전횟수를 출력하라
"""


def find_close_bus_station(max_cur, bus):   # 현재 위치에서 최대로 갈 수 있는 거리에서 가장 가까운 정류장
    close_station = 0
    for station in bus:
        if station <= max_cur:
            close_station = station
    return close_station


T = int(input())
for case in range(T):
    K, N, M = map(int, input().split())
    bus_lst = list(map(int, input().split()))

    count = 0
    cur = 0
    i = 0
    while cur < N:
        if cur + K >= N:    # 최대 거리가 끝이면 종료
            break
        close_station = find_close_bus_station(cur+K, bus_lst)
        if cur == close_station:    # 최대 거리에서 가까운 정류장을 구했는데 현재 위치와 같다면 움직일 수 없다는 뜻
            count = 0
            break
        cur = close_station     # 현재 위치를 가장 가까운 정류장으로 변경
        count += 1
    print(f'#{case+1} {count}')


