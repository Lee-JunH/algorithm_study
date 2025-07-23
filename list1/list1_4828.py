# swea - min max - D2

## N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

T = int(input())

def find_max(lst, N):
    lst_max = lst[0]
    for i in range(N):
        if lst_max <= lst[i]:
            lst_max = lst[i]
    return lst_max


def find_min(lst, N):
    lst_min = lst[0]
    for i in range(N):
        if lst_min >= lst[i]:
            lst_min = lst[i]
    return lst_min


for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{i+1}', find_max(lst, N) - find_min(lst, N))
