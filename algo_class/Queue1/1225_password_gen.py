"""
SWEA_1225 - 암호생성기 - D3

문제
- 8개의 숫자를 입력 받고 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
- 다음 첫 번째 수는 2 감소한 뒤 맨뒤로... 5까지 반복한다.
- 이와 같은 작업을 한 사이클이라 한다.
- 숫자가 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료한다.

출력
- 마지막 8자리 숫자를 출력

풀이
- 큐를 이용해 입력받고 작업 후 0 나오면 출력
"""


from collections import deque


T = 10
for _ in range(T):
    case = int(input())
    my_q = deque()
    my_q.extend(list(map(int, input().split())))

    i = 1
    while True:
        if i == 6:
            i = 1
        temp = my_q.popleft() - i
        if temp <= 0:
            my_q.append(0)
            break
        my_q.append(temp)
        i += 1
    print(f'#{case}', end=' ')
    print(*my_q)