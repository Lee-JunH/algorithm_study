"""
SWEA_1221 - GNS - D2

문제
- 숫자 체계가 "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"로 주어질 때
문자열이 주어질 때 작은 수부터 차례로 정렬하여 출력하라

풀이
- 딕셔너리로 값과 키를 나누고 카운팅 정렬로 정렬 후 출력
"""

T = int(input())
for tc in range(T):
    case = list(input().split())
    num_lst = list(input().split())
    number = [0 for _ in range(10)]

    my_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, \
               "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    my_dict2 = {value: key for key, value in my_dict.items()}
    for num in num_lst:
        number[my_dict[num]] += 1
    print(f'#{tc+1} ', end='')
    for i in range(10):
        for j in range(number[i]):
            print(my_dict2[i], end=' ')
    print()

# version 2 : 딕셔너리 안쓰고 풀기
# num_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())
# for tc in range(T):
#     _ = input()
#     num_lst = list(input().split())
#     number = [0 for _ in range(10)]
#     for num in num_lst:
#         for s in range(10):
#             if num == num_str[s]:
#                 number[s] += 1
#                 break
#     print(f'#{tc+1} ', end='')
#     for i in range(10):
#         for j in range(number[i]):
#             print(num_str[i], end=' ')
#     print()
