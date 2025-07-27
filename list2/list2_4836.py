# swea - 색칠하기 - D2

# '같은 색과는 곂치지 않는다'

T = int(input())        # T:testcase 개수

for i in range(T):
    N = int(input())    # N:사각형 개수
    board = [[0]*10 for _ in range(10)]     #이차원 배열 선언

    for _ in range(N):  # N만큼만 입력받기
        lst = list(map(int, input().split()))
        color = lst[4]
        for x in range(lst[0], lst[2] + 1):     # x축 범위
            for y in range(lst[1], lst[3] + 1): # y축 범위
                board[x][y] += color
    
    count = 0
    for x_list in board:
        for num in x_list:
            if num == 3:    # 보라색인 부분은 3
                count += 1
    
    print(f'#{i+1}', count)