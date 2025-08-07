"""
SWEA_4837 - 부분집합의 합 - D2

문제 설명
1부터 12까지의 숫자를 원소로 가진 집합 A에서 합이 K인 부분집합의 개수를 출력하라
"""

T = int(input())
for case in range(T):
    N, K = map(int, input().split())

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0
    for i in range(1 << 12):
        sum_prefix = 0
        sum_count = 0
        for j in range(12):
            if i & (1 << j):
                sum_prefix += num[j]
                sum_count += 1
        if sum_prefix == K and sum_count == N:
            count += 1
    print(f'#{case+1} {count}')

