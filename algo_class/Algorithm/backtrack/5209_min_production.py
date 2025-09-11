"""
SWEA_5209 - 최소 생산 비용 - D3

문제
- N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산한다
- 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 문제

풀이
- 일반적인 backtrack을 시행한다.
- 최소보다 더 큰 값이 나오면 리턴하도록 가지치기 하자
"""

def backtrack(factory, p):
    global min_price

    if p > min_price:
        return
    
    if factory == N:
        min_price = min(min_price, p)
    
    for i in range(N):
        if not production[i]:
            my_p = price[factory][i]
            production[i] = 1
            backtrack(factory+1, p + my_p)
            production[i] = 0

T = int(input())
for case in range(T):
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]

    min_price = 99*15
    production = [0] * N
    backtrack(0, 0)

    print(f'#{case+1} {min_price}')