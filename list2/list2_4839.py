# swea - 이진탐색 - D2

# 입력
## T : 테스트 케이스 개수
## P : 책의 전체 쪽 수
## A,B : 찾을 쪽 번호

T = int(input())

def binary_search(P, jjok):         #이진탐색 함수
    start = 1                       # 시작 위치
    end = P                         # 끝 위치
    center = (start + end) // 2     # 중앙 페이지
    count = 0
    while center != jjok:           # 목표를 찾을 때 까지 반복
        if center < jjok:           # 쪽이 더 크면 center ~ end
            start = center
        elif center > jjok:         # 쪽이 더 작으면 start ~ center
            end = center
        center = (start + end) // 2
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