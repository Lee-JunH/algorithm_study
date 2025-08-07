"""
SWEA_4839 - 이진탐색 - D2

문제 설명
책의 전체 쪽수와 두 사람이 찾을 족 번호가 주어졌을 때,
이진 탐색 게임에서 이긴 사람이 누구인지 알아내 출력하시오
"""


def binary_search(start, end, goal, count):
    center = (start + end) // 2
    count += 1
    if center == goal:
        return count
    elif center > goal:
        return binary_search(start, center, goal, count)
    elif center < goal:
        return binary_search(center, end, goal, count)
    return count 


T = int(input())
for case in range(T):
    P, A, B = map(int, input().split())

    count_A = binary_search(1, P, A, 0)
    count_B = binary_search(1, P, B, 0)
    print(f'#{case+1} ', end='')
    if count_A > count_B:
        print('B')
    elif count_A < count_B:
        print('A')
    else:
        print(0)

