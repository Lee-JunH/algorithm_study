# swea_4869 - 종이붙이기 - D2

T = int(input())

def func(N, count):
    if N == 0:
        return 1
    if N < 0:
        return 0
    count += func(N - 10, count) + 2 * func(N - 20, count)
    return count

for case in range(T):
    N = int(input())

    result = []
    i = 0
    j = 0
    count = func(N, 0) 
            
    print(f'#{case+1} {count}')