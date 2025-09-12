"""
SWEA_5293 - 이진 문자열 복원 - D3

문제
- N인 어떤 이진 문자열을 가지고 있다.
- 인접한 두 문자를 끊어 봤을 때 각각의 쌍이 몇 번씩 등장하는지를 적어 놓은 것이다.
- 단 인접한 두 문자를 귾어 볼 때 두칸씩 이동하지 않고 한칸만 이동하여 본다.

풀이
- '00', '01', '10', '11' 의 개수가 주어진다.
- 1개 이상 있는 경우의 수부터 배치를 해보면서 backtrack한다.
- 배치를 못하는 경우에는 리턴
- 확인하는 경우는 2가지로 1로 끝나는 경우, 0으로 끝나는 경우가 있다.
"""

T = int(input())
for case in range(T):
    count = list(map(int, input().split()))

    binary = ['00', '01', '10', '11']

    i = 0
    my_str = ''
    while True:
        if i == 4:
            break
        if count[i] != 0:
            if my_str == '':        # 처음에 값 넣기 위해서
                count[i] -= 1
                my_str = binary[i]
            elif my_str[0] == binary[i][1]:   # 앞에 넣을 수 있는 경우
                count[i] -= 1
                my_str = binary[i][0] + my_str
                i = 0
            elif my_str[-1] == binary[i][0]:   # 뒤에 넣을 수 있는 경우
                count[i] -= 1
                my_str = my_str + binary[i][1]
                i = 0
            else:
                i += 1
        else:
            i += 1
    if sum(count) != 0:
        print(f'#{case+1} impossible')
    else:
        print(f'#{case+1} {my_str}')


# def backtrack(my_str):
#     global check, result

#     if sum(count) == 0:
#         check = 1
#         result = my_str
#         return

#     if my_str[-1] == '0' and count[0] == 0 and count[1] == 0:
#         return
#     if my_str[-1] == '1' and count[2] == 0 and count[3] == 0:
#         return
    
#     for i in range(4):
#         if count[i] != 0:
#             if my_str[-1] == binary[i][0]:
#                 count[i] -= 1
#                 backtrack(my_str + binary[i][1])
#                 if check:
#                     return
#                 count[i] += 1