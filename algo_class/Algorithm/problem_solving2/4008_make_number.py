"""
SWEA_4008 - 숫자 만들기 - 모듸 SW 역량테스트

문제
- N개의 숫자가 적혀있는 게임 판이 있고, +,-,*,/ 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과값을 구해보기로 한다.
- 연산자의 우선순위는 고려하지 않고 왼쪽에서 오른쪽으로 계산한다.
- 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하는 문제
"""

def recur(cnt, total, plus, minus, mul, div):
    global min_result
    global max_result

    if cnt == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    if plus > 0:
        recur(cnt+1, total+number[cnt], plus-1, minus, mul, div)
    if minus > 0:
        recur(cnt+1, total-number[cnt], plus, minus-1, mul, div)
    if mul > 0:
        recur(cnt+1, total*number[cnt], plus, minus, mul-1, div)
    if div > 0:
        recur(cnt+1, int(total/number[cnt]), plus, minus, mul, div-1)


T = int(input())
for case in range(T):
    N = int(input())
    oper = list(map(int, input().split()))
    number = list(map(int, input().split()))

    min_result = 1e9
    max_result = -1e9

    recur(1, number[0], oper[0], oper[1], oper[2], oper[3])

    print(f'#{case+1} {max_result - min_result}')