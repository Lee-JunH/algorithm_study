"""
SWEA_1952 - 수영장 - 모의 SW 역량 테스트

문제
- 수영장 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때
- 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고, 그 비용을 출력하는 문제

풀이
- 먼저 각 달마다 1일가격으로 계산한다.
- 그다음 한달 가격과 비교해서 업데이트 한다.
"""

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
    
    min_hap = [0 for _ in range(12)]
    min_hap[0] = min(month3, price[0])
    for i in range(1, 12):
        if i < 3:
            min_hap[i] = min(month3, min_hap[i-1] + price[i])
        else:
            min_hap[i] = min(min_hap[i-3]+month3, min_hap[i-1] + price[i])

    if min_hap[11] > year:
        print(f'#{case+1} {year}')
    else:    
        print(f'#{case+1} {min_hap[11]}')


# 재귀로 푸는 방식 (강의)

# 종료 조건 : 12월 을 모두 고려한 경우
# 가지의 수 : 4개 (일, 달, 달3, 년)

# def recur(month, total):
#     global min_answer
#     if month > 12:
#         min_answer = min(min_answer)
#         return
#     # 1일권으로 사는 경우
#     recur(month+1, total + (days[month]*day))
#     # 1달권으로 사는 경우
#     recur(month+1, total + month1)
#     # 3달권으로 사는 경우
#     recur(month+3, total + month3)
#     # 1년으로 사는 경우
#     recur(month+12, total + year)