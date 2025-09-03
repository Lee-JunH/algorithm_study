"""
SWEA_18593 - 2진수를 10진수로 출력하기 - D2

문제
- 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기
"""

def bin_to_decimal(bin):
    decimal = 0
    for i in range(7):
        if bin[i] == 1:
            decimal += 2 ** (6-i)
    return decimal

T = int(input())
for case in range(T):
    N = int(input())
    num_str = []
    for i in range(N):
        num_str.extend(list(map(int, input().strip())))

    print(f'#{case+1}', end=' ')
    for j in range(0, N*10, 7):
        check = num_str[j:j+7]
        print(bin_to_decimal(check), end=' ')
    print()