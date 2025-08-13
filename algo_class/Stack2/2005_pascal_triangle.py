"""
SWEA_2005 - 파스칼의 삼각형 - D2

문제
- 크기가 N인 파스칼의 삼각형을 만든다.
- 조건
    - 첫 번째 줄은 항상 숫자 1
    - 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합

출력
- N을 입력 받아 크기 N인 파스칼의 삼각형 출력

풀이
- 그냥 하나씩 넣자. 규칙X
"""

T = int(input())
for case in range(T):
    N = int(input())

    pascal = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if i-1 < 0 or j-1 < 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print(f'#{case+1}')
    for p in pascal:
        for n in p:
            if n == 0:
                break
            print(n, end=' ')
        print()