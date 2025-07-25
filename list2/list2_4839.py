# swea - 이진탐색 - D2

# 입력
## T : 테스트 케이스 개수
## P : 책의 전체 쪽 수
## A,B : 찾을 쪽 번호

T = int(input())

def binary_search(P, jjok):
    first = 1
    last = P
    center = (1 + P) // 2
    count = 0
    while center != jjok:
        if center < jjok:
            first = center
        elif center > jjok:
            last = center
        center = (first + last) // 2
        count += 1
    return count


for i in range(T):
    P, A, B = map(int, input().split())

    count_A = binary_search(P, A)
    count_B = binary_search(P, B)
    print(f'#{i+1}', end=' ')
    if count_A < count_B:
        print('A')
    elif count_A > count_B:
        print('B')
    else:
        print(0)