"""
SWEA_5097 - 회전 - D2

문제 설명
N개의 숫자로 이루어진 수열이 주어진다.
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때 수열의 맨 앞에 있는 숫자를 출력

풀이
첫 번째 값을 M번 보내고 맨 앞의 숫자 출력
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    my_queue = list(map(int, input().split()))

    count = M - N * (M // N)   # 최소 반복 횟수 계산하여 빼주기
    print(f'#{case+1} {my_queue[count]}')

