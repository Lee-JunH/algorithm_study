"""
SWEA_2819 - 격자판의 숫자 이어 붙이기 - D4

문제
- 4x4 격자판에 0~9 사이의 숫자가 적혀있다.
- 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 6번 이동하면서
- 각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
- 이동할 때 한 번 거쳤던 격자칸을 다시 지나도 되며, 0으로 시작하는 수도 만들 수 있다.
- 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하시오.
"""

# 종료조건 : 숫자 7자리일 때 종료
# 가지의 수 : 4개
def recur(r, c, number):
    if len(number) == 7:
        result.add(number)
        return

    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]

        if nc < 0 or nc >= 4 or nr < 0 or nr >= 4:
            continue
        recur(nr, nc, number + matrix[nr][nc])

T = int(input())
for case in range(T):
    matrix = [input().split() for _ in range(4)]
    result = set()

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(4):
        for j in range(4):
            recur(i, j, matrix[i][j])

    print(f'#{case+1} {len(result)}')