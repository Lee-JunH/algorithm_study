# swea - 특별한 정렬 - D3

# 10 1 9 2 8 3 7 4 6 5 로 정렬
# 출력은 10개만

T = int(input())

for i in range(T):
    N = int(input())
    not_sort = list(map(int, input().split()))

    print(f'#{i + 1}', end=' ')
    for j in range(1, 11):
        if j % 2 == 1:      # 홀수 번호 : 리스트에서 작은 수
            print(max(not_sort), end=' ')   # max()로 가장 큰값 출력
            not_sort.remove(max(not_sort))  # max 값은 리스트에서 삭제
        else:               # 짝수 번호 : 리스트에서 큰 수
            print(min(not_sort), end=' ')   # min()로 가장 작은 값 출력
            not_sort.remove(min(not_sort))  # min 값은 리스트에서 삭제
    print()


# 내장 함수 없는 버전

# def find_max(lst):
#     lst_max = lst[0]
#     for num in lst:
#         if lst_max <= num:
#             lst_max = num
#     return lst_max

# def find_min(lst):
#     lst_min = lst[0]
#     for num in range(N):
#         if lst_min >= num:
#             lst_min = num
#     return lst_min

# T = int(input())

# for i in range(T):
#     N = int(input())
#     not_sort = list(map(int, input().split()))

#     print(f'#{i + 1}', end=' ')
#     for j in range(1, 11):
#         if j % 2 == 1:      # 홀수 번호 : 리스트에서 작은 수
#             print(find_max(not_sort), end=' ')
#             not_sort.remove(find_max(not_sort))
#         else:               # 짝수 번호 : 리스트에서 큰 수
#             print(find_min(not_sort), end=' ')
#             not_sort.remove(find_min(not_sort))
#     print()