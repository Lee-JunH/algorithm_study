"""
SWEA_5099 - 피자굽기 - D2

문제
- N개의 피자를 동시에 구울 수 있는 화덕이 있다.
- 치즈가 모두 녹으면 화덕에서 꺼낸다.
- M개의 피자를 순서대로 화덕에 넣을 때 화덕에 가장 마지막에 남아있는 피자 번호는?
- 조건
    - 피자는 1번 위치에서 넣거나 뺄 수 있다.
    - 화덕에서 피자는 회전한다.
    - 한바퀴 돈 치즈는 C // 2로 줄어든다.
    - 치즈가 녹아 0이 되면 화덕에서 꺼내고 다음 피자를 넣는다.

출력
- 마지막 남은 피자의 번호를 출력

풀이
- 큐의 구조와 같다. 맨 앞의 값을 확인하고 다시 넣을 때 반 나눠서 넣어주면 된다.
- 0인 경우는 다시 넣지 않고 큐의 크기가 1일 때 종료하여 출력한다.
"""

from collections import deque

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    cheeze = list(enumerate(map(int, input().split()), start=1))

    pizza = deque(cheeze[:N])   # 화덕에 피자 N개 넣기
    while len(pizza) != 1:     # 화덕에 1개 남을 때 까지
        temp = pizza.popleft()     # 1번 자리 확인
        if temp[1] == 0:            # 치즈가 0일 때
            if N != M:              # 넣을 피자가 남았으면 더 넣기
                N += 1
                pizza.append((cheeze[N-1][0], cheeze[N - 1][1] // 2))
        else:
            pizza.append((temp[0], temp[1] // 2))
    print(f'#{case+1} {pizza.pop()[0]}')