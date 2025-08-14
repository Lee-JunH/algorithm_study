"""
SWEA_1222 - 계산기1 - D4

문제
- 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하시오

풀이
- 그냥 더한다
"""

T = 10
for case in range(T):
    cal_len = int(input())
    cal_str = input()

    cnt = 0
    temp = 0
    result = 0
    for num in cal_str:
        if num == '+':
            result += temp
            cnt = 0
            temp = 0
        else:
            temp = temp * (10**cnt) + int(num)
            cnt = 1
    result += temp
    print(f'#{case+1} {result}')