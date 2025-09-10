"""
SWEA - 9386
연속된 1의 개수
"""

T = int(input())

for case in range(T):
    N = int(input())
    num = input()

    count = 0
    max_count = 0
    for one in num:
        if one == '1':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(f'#{case+1} {max_count}')

