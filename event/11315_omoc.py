#SWEA_11315 - 오목 판정 - D3

def check(omoc):
    count3 = 0
    for i in range(N):
        count = 0
        count2 = 0
        for j in range(N):
            if omoc[i][j] == 'o':
                count += 1
            else:
                if count >= 5:
                    return 'YES'
                count = 0
            if omoc[j][i] == 'o':
                count2 += 1
            else:
                if count2 >= 5:
                    return 'YES'
                count2 = 0
        if count >= 5 or count2 >= 5:
            return 'YES'
    return 'NO'

def cross(omoc, r, c):
    count = 0
    count2 = 0
    for i in range(N):
        for j in range(N):
            if i + j == r + c and omoc[i][j] == 'o':
                count += 1
            elif i + j == r + c and omoc[i][j] == '.':
                if count >= 5:
                    return 'YES'
                count = 0
            
            if i - j == r - c and omoc[i][j] == 'o':
                count2 += 1
            elif i - j == r - c and omoc[i][j] == '.':
                if count2 >= 5:
                    return 'YES'
                count2 = 0
    if count >= 5 or count2 >= 5:
            return 'YES'
    return 'NO'

T = int(input())
for case in range(T):
    N = int(input())
    omoc = [list(input().strip()) for _ in range(N)]

    result = check(omoc)
    if result == 'NO':
        for i in range(N):
            for j in range(N):
                result = cross(omoc, i, j)
                if result == 'YES':
                    break
            if result == 'YES':
                break

    print(f'#{case+1} {result}')