"""
SWEA_1952 - 수영장 - 모의 SW 역량 테스트

문제
- 수영장 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때
- 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고, 그 비용을 출력하는 문제

풀이
- 먼저 각 달마다 1일가격으로 계산한다.
- 그다음 한달 가격과 비교해서 업데이트 한다.
- 
"""

def dfs(idx, hap):
    global result

    if idx == 14:
        result = min(result, hap)

    if result < hap:
        return

    for i in range(idx, 14):
        hap3 = 0
        for j in range(i-2, i+1):
            if j >= 12 or j < 0 or price[j] == 0:
                continue
            hap3 += price[j]
        if hap3 == 0:
            continue
        if hap3 > month3:
            dfs(i+3, hap+month3)
        else:
            if i-2 >= 0:
                dfs(i+1, hap+price[i-2])
            else:
                dfs(i+1, hap)

T = int(input())
for case in range(T):
    day, month1, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))

    price = [0] * 12
    for i in range(12):
        day_price = plan[i] * day
        if day_price < month1:
            price[i] = day_price
        else:
            price[i] = month1
    print(*price)
    
    result = sum(price)

    if result > year:
        result = year
    print(f'#{case+1} {result}')