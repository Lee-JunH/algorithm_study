# swea - 부분집합의 합 - D3

# 부분집합 : 합이 8인 경우 ex) {1,2,5}, {1,3,4}


T = int(input())        # testcase 개수

for i in range(T):
    N, K = map(int, input().split())

    count = 0
    lst = [[0] for x in range(12)]      # bit리스트 활용
    print(f'#{i+1}', count)


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