"""
SWEA_11092 - 최대 최소의 간격 - D1

문제 설명
N개의 양의 정수에서 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력
"""

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    max_num = lst[0]
    min_num = lst[0]
    max_index = 0
    min_index = 0
    for i in range(len(lst)):
        if lst[i] >= max_num:
            max_num = lst[i]
            max_index = i
        elif lst[i] < min_num:
            min_num = lst[i]
            min_index = i
    result = max_index - min_index
    if result < 0:
        result *= -1
    print(f'#{case+1} {result}')

