"""
SWEA_4881 - 배열 최소 합 - D2

문제 설명
> NxN 배열에서 한 줄에 하나씩 골라 합이 최소가 되도록 한다.
> 단, 세로로 같은 줄에서 2개 이상의 숫자를 고를 수 없다.
"""


def check_line(arr, num, row, sum_one, min_sum):
    if sum_one >= min_sum:
        return min_sum
    if row == N:
        if sum_one < min_sum:
            min_sum = sum_one
            return min_sum
    for col in range(N):
        if num[col] == 0:
            num[col] = 1
            min_sum = check_line(arr, num, row+1, sum_one + arr[row][col], min_sum)
            num[col] = 0
    return min_sum


T = int(input())
for case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    num = [0] * N   # 그 열을 사용했는지 체크할 배열
    min_sum = check_line(arr, num, 0, 0, 90)
    print(f'#{case+1} {min_sum}')