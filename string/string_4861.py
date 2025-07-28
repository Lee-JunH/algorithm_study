# swea - 회문 - D2

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    finded = 0

    lst = []
    for _ in range(N):
        lst.append(input())
    print(f'#{case+1} ', end='')
    for i in range(N):
        new_lst = [lst[i][x] for x in range(N)]
        for t in range(N - M + 1):
            temp1 = new_lst[t : M // 2 + t]
            if M % 2 == 0:
                temp2 = new_lst[(M - 1) + t : M // 2 - 1 + t : -1]
            else:
                temp2 = new_lst[(M - 1) + t : M // 2 + t : -1]
            if temp1 == temp2:
                for i in range(t, t+M):
                    print(new_lst[i], end='')
                finded = 1
                print()
                break
    if finded == 0:
        for j in range(N):
            new_lst = []
            new_lst = [lst[y][j] for y in range(N)]
            for t2 in range(N - M + 1):
                temp3 = new_lst[t2 : M // 2 + t2]
                if M % 2 == 0:
                    temp4 = new_lst[(M - 1) + t2 : M // 2 - 1 + t2 : -1]
                else:
                    temp4 = new_lst[(M - 1) + t2 : M // 2 + t2 : -1]
                if temp3 == temp4:
                    for i in range(t, t+M):
                        print(new_lst[i], end='')
                    print()
                    break