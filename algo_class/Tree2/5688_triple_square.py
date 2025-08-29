"""
SWEA_5688 - 세제곱근을 찾아라 - D3

문제
- 양의 정수 N에 대해 N = X^3가 되는 양의 정수X를 구하라
- 존재하지 않으면 -1 출력

풀이
- 3번 곱했을 때 N이 되는 수를 찾는 것이다.
- N을 어떤 수로 3번 나눳을 때 1이 되는 경우를 찾자.
- 또는 3번 곱햇을 때 N인 수를 찾자
"""

T = int(input())
for case in range(T):
    N = int(input())
    result = -1
    for i in range(1, N//3 + 2):
        if i*i*i == N:
            result = i
            break
        elif i*i*i > N:
            result = -1
            break
    print(f'#{case+1} {result}')

