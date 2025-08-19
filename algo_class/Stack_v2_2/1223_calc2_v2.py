"""
SWEA_1223 - 계산기2 - D4

문제
- 문자열로 이루어진 계산식이 주어질 때, 후의 표기식으로 바꾸어 계산하는 프로그램을 만들어라

출력
- 계산 결과
"""


T = 10
for case in range(T):
    N = int(input())
    cal_str = input().strip()

    op = 0
    temp = 0
    result = 0
    stack = []
    for num in cal_str:
        if num == '+':
            op = 0
            result += temp
        elif num == '*':
            op = 1
            stack.append(temp)
        else:
            temp = int(num)
            while stack:
                a = stack.pop()
                temp *= a
    result += temp
    print(f'#{case+1} {result}')

