'''
SWEA_4874번 - Forth - D2

문제 설명
- 후위 표기법으로 숫자, 연산자(+-*/), '.' 을 입력받아 결과를 출력
'''

T = int(input())
for case in range(T):
    lst = input().split()

    my_stack = []       # 스택 선언
    for data in lst:
        if data in '+-/*':          # 1. 연산자인 경우
            if len(my_stack) < 2:       # 연산자 앞에 숫자 2개가 없는 경우 error
                result = 'error'
                break
            else:                       # pop 2번 하여 숫자 계산 후 스택에 입력
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                if data == '+':
                    num3 = num2 + num1
                elif data == '-':
                    num3 = num2 - num1
                elif data == '*':
                    num3 = num2 * num1
                elif data == '/':
                    num3 = num2 // num1
                my_stack.append(num3)
        elif data == '.':           # 2. 종료인 경우
            if len(my_stack) > 1:       # 출력 값 외에 다른 값들이 있으면 error
                result = 'error'
            else:                       # 결과 값 pop으로 저장
                result = my_stack.pop()
        else:                       # 3. 그외 숫자인 경우
            my_stack.append(int(data))  # 스택에 입력
    print(f'#{case+1} {result}')


# ver2
# def calculate(my_stack, data):
#     try:
#         temp1 = my_stack.pop()
#         temp2 = my_stack.pop()
#     except IndexError:
#         return 'error'
#     else:
#         if data == '+':
#             return temp2 + temp1
#         elif data == '-':
#             return temp2 - temp1
#         elif data == '*':
#             return temp2 * temp1
#         elif data == '/':
#             return temp2 // temp1

# T = int(input())
# for case in range(T):
#     lst = input().split()

#     my_stack = []
#     for data in lst:
#         if data in '+-/*':
#             result = calculate(my_stack, data)
#             if result == 'error':
#                 break
#             else:
#                 my_stack.append(result)
#         elif data == '.':
#             if len(my_stack) > 1:
#                 result = 'error'
#             else:
#                 result = my_stack.pop()
#         else:
#             my_stack.append(int(data))
#     print(f'#{case+1} {result}')