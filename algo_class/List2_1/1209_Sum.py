"""
SWEA_1209 - Sum - D3

문제 설명
2차원 배열이 주어질 때 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라
"""


def max_sum(lst):
    max_value = 0
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


T = 10
for _ in range(T):
    case = int(input())
    arr = [[0]*100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    sum_arr = []
    sum_cross1 = 0
    sum_cross2 = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
            if i == j:
                sum_cross1 += arr[i][j]
            if i + j == 99:
                sum_cross2 += arr[i][j]
        sum_arr.extend([sum_row, sum_col])
    sum_arr.extend([sum_cross1, sum_cross2])
    print(f'#{case} {max_sum(sum_arr)}')
