"""
SWEA_1974 - 스도쿠 검증 - D2

문제 설명
9X9 크기의 스도쿠 퍼즐의 숫자가 주어졌을 때, 겹치는 숫자가 없는지 확인하고 1또는 0을 출력하라
"""


def check_sdoku1(sdoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            number = []
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if sdoku[row][col] not in number:
                        number.append(sdoku[row][col])
                    else:
                        return 0
    return 1


def check_sdoku2(sdoku):
    for i in range(9):
        number = []
        number2 = []
        for j in range(9):
            if sdoku[i][j] not in number:
                number.append(sdoku[i][j])
            else:
                return 0
            if sdoku[j][i] not in number2:
                number2.append(sdoku[j][i])
            else:
                return 0
    return 1


T = int(input())
for case in range(T):
    sdoku = [list(map(int, input().split())) for _ in range(9)]

    check = check_sdoku1(sdoku)
    check += check_sdoku2(sdoku)
    if check == 2:
        check = 1
    else:
        check = 0
    print(f'#{case+1} {check}')

