"""
SWEA_1859 - 백만장자 프로젝트 - D2

문제
- 사재기를 하여 최대한의 이득을 얻도록 한다.
- 조건
    - 연속된 N일 동안의 물건 매매가를 알고있다.
    - 하루에 최대 1개 구입 가능
    - 판매는 얼마든지 가능
- ex) 3일 동안의 매매가가 1,2,3 일 때, 처음 두 날에 원료 구매 후 마지막날에 팔면 3의 이득

출력
- 최대 이익 출력

풀이
- 살 때는 stack에 push하고 팔 때는 pop하며 차이 계산
"""

# def find_max(lst):
#     max_n = 0
#     for n in lst:
#         if max_n < n:
#             max_n = n
#     return max_n


# T = int(input())
# for case in range(T):
#     N = int(input())
#     price = list(map(int, input().split()))

#     max_num = find_max(price)
#     total = 0
#     for i in range(N):
#         if price[i] == max_num:
#             max_num = find_max(price[i+1:])
#         else:
#             total += max_num - price[i]
#     print(f'#{case+1} {total}')

T = int(input())
for case in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    count = 0
    total = 0
    my_stack = []
    for i in range(N):
        if my_stack:
            temp = my_stack.pop()
            if temp > price[i]:
                count = 0
            else:
                count += 1
                total += (price[i] - temp) * count
            my_stack.append(price[i])
        else:
            my_stack.append(price[i])
    print(f'#{case+1} {total}')