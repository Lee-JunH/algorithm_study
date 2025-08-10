# SWEA_9386 - 연속한 1의 개수 - D1

T = int(input())
for case in range(T):
    N = int(input())
    sequence = input()

    count = 0
    max_count = 0
    for i in range(N):
        if sequence[i] == '1':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    
    print(f'#{case+1} {max_count}')

