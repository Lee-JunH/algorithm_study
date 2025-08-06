"""
SWEA - 4835
구간합
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))

    sum_prefix = 0
    for i in range(M):
        sum_prefix += num_lst[i]
    min_prefix = sum_prefix
    max_prefix = sum_prefix
    for i in range(N - M):
        sum_prefix = sum_prefix + num_lst[M + i] - num_lst[i]
        if sum_prefix > max_prefix:
            max_prefix = sum_prefix
        elif sum_prefix < min_prefix:
            min_prefix = sum_prefix
    print(f'#{case+1} {max_prefix - min_prefix}')

