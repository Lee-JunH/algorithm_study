"""
SWEA_10761 - 신뢰 - D3

3:16
문제
- 서로 다른 복도에 두 로봇이 있다.
- 한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼이 존재
- 버튼 K는 복도의 시작점에서 K미터 떨어져 있다.
- 두 로봇은 버튼 1에서 시작
    - 매 1초마다, 로봇은 복도의 양 방향 중 하나로 1미터 걷거나,
    - 자기 위치에 있는 버튼을 누르거나
    - 아무것도 하지 않는다.
- O x는 오렌지가 x버튼을 눌러야 함을 뜻함, B x는 블루가 눌러야 함을 뜻함

출력
- 테스트를 끝낼 수 있는 가장 빠른 시간

풀이
- 자기 위치 인덱스의 값 check하고 1이면 머물고 아니면 이동하기
"""

TC = int(input())
for case in range(TC):
    input_lst = list(input().split())
    N = int(input_lst[0])
    button = input_lst[1:]

    i = 0
    O_i = 1
    B_i = 1
    move = 0
    temp_B = 0
    temp_O = 0
    count_button = 0
    while count_button != N:
        if button[i] == 'B':
            if temp_O >= int(button[i+1]) and prev == 'O':
                move += 1
                B_i = int(button[i+1])
            else:
                move += abs(int(button[i+1]) - B_i) + 1
                B_i = int(button[i+1])
            temp_B = int(button[i+1])
            prev = 'B'

            
        elif button[i] == 'O':
            if temp_B >= int(button[i+1]) and prev == 'B':
                move += 1
                O_i = int(button[i+1])
            else:
                move += abs(int(button[i+1]) - O_i) + 1
                O_i = int(button[i+1])
            temp_O = int(button[i+1])
            prev = 'O'
        i += 2
        count_button += 1
    print(f'#{case+1} {move}')

