# swea - 구간합 - D2

T = int(input())

def find_max_min(lst, N, M):
    sum_close = 0
    for i in range(M):          #첫 M개의 합 구하기
        sum_close += lst[i]
    sum_max = sum_close         #초기 max값
    sum_min = sum_close         #초기 min값
    for j in range(M, N):
        sum_close = sum_close + lst[j] - lst[j - M]     #ex) 1,2,3 합에서 1,2,3 + 4 - 1 = 2,3,4
        if sum_max <= sum_close:    #max 찾기
            sum_max = sum_close
        if sum_min >= sum_close:    #min 찾기
            sum_min = sum_close
    return [sum_max, sum_min]


for i in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    result = find_max_min(lst, N, M)
    print(f'#{i+1}', result[0] - result[1])