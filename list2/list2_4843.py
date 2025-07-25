# swea - 특별한 정렬 - D3

# 10 1 9 2 8 3 7 4 6 5 로 정렬
# 출력은 10개만

T = int(input())

for i in range(T):
    N = int(input())
    not_sort = list(map(int, input().split()))

    print(f'#{i + 1}', end=' ')
    for j in range(1, 11):
        if j % 2 == 1:
            print(max(not_sort), end=' ')
            not_sort.remove(max(not_sort))
        else:
            print(min(not_sort), end=' ')
            not_sort.remove(min(not_sort))
    print()