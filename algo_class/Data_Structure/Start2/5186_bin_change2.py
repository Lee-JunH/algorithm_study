"""
SWEA_5186 - 이진수2 - D2

문제
- 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다.
- N을 소수점 아래 12자리 이내로 표시할 수 있으면 0.을 제외한 나머지 숫자 출력
- 13자리 이상인 경우 overflow출력
"""

from collections import deque

def change(bin):
    i = 1
    while bin != 0:
        if 2**(-i) <= bin:
            my_q.append(1)
            bin -= 2**(-i)
        else:
            my_q.append(0)
        i += 1
    if len(my_q) >= 13:
        print('overflow', end='')
    else:
        while my_q:
            print(my_q.popleft(), end='')

T = int(input())
for case in range(T):
    num = float(input())

    my_q = deque()

    print(f'#{case+1}', end=' ')
    change(num)
    print()