"""
SWEA - 1206
min-max
"""

T = int(input())
for case in range(T):
    N = int(input())
    num_lst = list(map(int, input().split()))

    max_num = num_lst[0]
    min_num = num_lst[0]
    for num in num_lst:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    print(f'#{case+1} {max_num - min_num}')
