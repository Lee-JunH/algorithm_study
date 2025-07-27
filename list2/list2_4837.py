# swea - 부분집합의 합 - D3

# 부분집합 : 합이 8인 경우 ex) {1,2,5}, {1,3,4}

# 1. 모든 부분집합을 찾아서 합이 K인 경우 찾기

# 비트연산을 이용해서 
# 0 0 0 1 이면 4
# 1 1 1 1 이면 1 2 3 4 

T = int(input())

lst = [x for x in range(1, 13)]      # bit리스트 활용
for case in range(T):
    N, K = map(int, input().split())

    count = 0
    for i in range(1<<12):
        temp_lst = []
        for j in range(12):
            if i & (1<<j):
                temp_lst.append(lst[j])
        if len(temp_lst) == N and sum(temp_lst) == K:
            count += 1
    print(f'#{case+1}', count)


# count = 0
# lst = []
# num = 1
# while num < 13:
#     if len(lst) != N:
#         lst.append(num)
#         num += 1
#     else:
#         if sum(lst) == K:
#             count += 1
#             lst.pop()
#             num = lst.pop() + 1
#         else:
#             lst.pop()