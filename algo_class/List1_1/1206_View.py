"""
SWEA - 4828
View
"""


def check_building(bd, index):
    high = 0
    for back in range(-2, 3):
        if back == 0:
            continue
        if high < bd[index + back]:
            high = bd[index + back]
    dif = bd[index] - high
    if dif > 0:
        return dif
    else:
        return 0


for case in range(10):
    N = int(input())
    building = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        count += check_building(building, i)
    print(f'#{case+1} {count}')

