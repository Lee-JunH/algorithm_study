"""
SWEA_5202 - 화물 도크 - D3

문제
- 0시부터 다음날 0시 이전까지 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면
- 몇 대의 화물차가 이용할 수 있는지 알아내는 문제 
- 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있다.
- 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.

풀이
- 최대 차 개수를 구하는 거니까 dfs로 하나씩 선택해 본다.
"""

def dfs(index, truck):
    global max_truck

    if index == N-1:
        max_truck = max(max_truck, truck)
    for i in range(index+1, N):
        if time[index][1] >= time[i][0]:
            dfs(i, truck+1)
        if i == N-1:
            max_truck = max(max_truck, truck)

T = int(input())
for case in range(T):
    N = int(input())
    time = []
    for _ in range(N):
        s, e = map(int, input().split())
        time.append([e,s])
    time.sort(reverse=True)

    max_truck = 1
    for i in range(N-1):
        dfs(i, 1)
    print(f'#{case+1} {max_truck}')