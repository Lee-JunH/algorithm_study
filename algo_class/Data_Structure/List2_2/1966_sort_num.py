"""
SWEA_1966 - 숫자를 정렬하자 - D2

문제 설명
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라
"""


def selection(N, num):
    for i in range(N - 1):
        min_idx = i
        for j in range(i+1, N):
            if num[min_idx] > num[j]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]
    return num


T = int(input())
for case in range(T):
    N = int(input())
    num_lst = list(map(int, input().split()))

    result = selection(N, num_lst)
    print(f'#{case+1} ', end='')
    for i in range(N):
        print(result[i], end=' ')
    print()

