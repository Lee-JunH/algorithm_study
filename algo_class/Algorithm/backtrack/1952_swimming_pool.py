"""
SWEA_1952 - 수영장 - 모의 SW 역량 테스트

문제
- 수영장 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때
- 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고, 그 비용을 출력하는 문제

풀이
- 
"""

T = int(input())
for case in range(T):
    day, month1, month3, year = map(int, input().split())
    plan = list(map(int, input().split()))

    