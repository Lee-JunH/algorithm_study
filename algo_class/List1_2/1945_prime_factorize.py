"""
SWEA_1945 - 간단한 소인수분해 - D2

문제 설명
- N = 2^a * 3^b * 5^c * 7^d * 11^e 이다. a, b, c, d, e를 출력하라
"""

T = int(input())
for case in range(T):
    N = int(input())

    lst_num = [0, 0, 0, 0, 0]
    while N != 0:
        if N % 2 == 0:
            N = N // 2
            lst_num[0] += 1
        elif N % 3 == 0:
            N = N // 3
            lst_num[1] += 1
        elif N % 5 == 0:
            N = N // 5
            lst_num[2] += 1
        elif N % 7 == 0:
            N = N // 7
            lst_num[3] += 1
        elif N % 11 == 0:
            N = N // 11
            lst_num[4] += 1
        else:
            break
    print(f'#{case+1}', end=' ')
    for num in lst_num:
        print(num, end=' ')
    print()

