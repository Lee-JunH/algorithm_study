"""
SWEA_5099 - 피자 굽기 - D3

문제
- 화덕에서 N개의 피자를 동시에 구울 수 있다.
- M개의 피자를 순서대로 화덕에 넣을 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 출력
- 조건
    - 1번 위치에서 넣거나 뺄 수 있다.
    - 1번에서 꺼내 치즈를 확인하고 다시 넣을 수 있다.
    - 화덕을 한 바퀴 돌 때 녹지 않은 치즈의 양은 반으로 준다. (C//2)
    - 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고 남은 피자를 그 자리에 넣는다.

출력
- 마지막까지 남아있는 피자 번호 출력

풀이
- 7 2 6 -> 3 1 3 -> 1 0 1
- queue를 만들어 pop하고 다시 push해주면 됨.
- 위치1에 있는 피자가 0인 경우 빼고 다음 피자를 넣는다.
- queue에 하나 남을 때까지 반복한다.
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    pizza_lst = list(map(int, input().split()))
    
    my_queue = pizza_lst[:N].copy() # 화덕에 N개만큼 미리 넣기
    final_num = [x for x in range(1, N+1)]  # 인덱스를 저장할 큐 생성
    rotate = 0  # 회전 횟수

    i = N
    pizza = N   # 현재 화덕에 있는 피자 개수
    while len(my_queue) != 1:
        temp = my_queue.pop(0)      # 첫 번째 값 확인
        num_temp = final_num.pop(0)
        if temp == 0:
            if len(pizza_lst) != i:   # 0이고 더 넣을 피자 넣기
                my_queue.append(pizza_lst[i] // 2)  # 넣고 돌릴거니까 넣을 때 나누기
                final_num.append(i+1)
                i += 1
        else:   # 확인 했던 피자 다시 뒤에 넣어주기
            my_queue.append(temp // 2)  # 넣고 돌릴거니까 넣을 때 나누기
            final_num.append(num_temp)

    print(f'#{case+1} {final_num.pop(0)}')

