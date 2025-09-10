"""
SWEA_9367 - 점점 커지는 당근의 개수 - D1

문제 설명
연속으로 커지는 당근 개수의 최대값을 출력
"""

T = int(input())
for case in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))

    start = carrot[0]
    max_count = 0
    count = 1
    for i in range(1, N):
        if start < carrot[i]:
            count += 1
            start = carrot[i]
        else:
            if max_count < count:
                max_count = count
            count = 1
            start = carrot[i]
    if max_count < count:
        max_count = count
    print(f'#{case+1} {max_count}')

