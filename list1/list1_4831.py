# swea - 전기버스 - D3

T = int(input())

# K : 최대 이동 가능 수
# N : 최종 목적지 번호
# M : 충전기 개수
# bus_charging : 충전기 번호

## 어떻게 풀까?
## 내 위치부터 제일 가까운 충전기 위치까지 거리 계산해 놓고
## 최대 이동 가능 수(K)와 비교해서 
## 

def find_stop(bus, K, N, M):
    pos = 0
    count = 0
    temp = 0
    for i in range(M):
        if pos + K >= N:    #현재 위치에서 바로 갈 수 있는 경우
            return count
        if bus[i] - pos < K:    #더 갈 수 있는 경우
            temp = bus[i]
        elif bus[i] - pos == K: #최대 이동 위치에 충전소인 경우
            pos = bus[i]
            count += 1
        elif bus[i] - pos > K:  #더 못가는 경우
            if temp + K >= bus[i]:     #거리가 너무 먼 경우
                pos = temp
                temp = bus[i]
                count += 1
            else:
                return 0
    if pos + K >= N:
        return count
    elif temp + K >= N:
        return count + 1
    return 0


for i in range(T):
    K, N, M = map(int, input().split())
    bus_charging = []
    bus_charging = list(map(int, input().split()))
    result = find_stop(bus_charging, K, N, M)
    print(f'#{i+1}', result)