"""
SWEA_1979 - 어디에 단어가 들어갈 수 있을까 - D2

문제 설명
NXN 크기의 단어 퍼즐을 만들려고 한다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리 수를 출력하라
"""


def line(lst, K):
    temp = lst.copy()
    count = 0
    go = 0
    while temp:
        num = temp.pop()
        if num == 1:
            count += 1
        elif num == 0:
            if count == K:
                go += 1
            count = 0
    if count == K:
        go += 1
    return go


T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    puzzle_garo = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        result += line(puzzle_garo[i], K)
    for sero in zip(*puzzle_garo):
        result += line(list(sero), K)
    print(f'#{case+1} {result}')


