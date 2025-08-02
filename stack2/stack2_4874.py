'''
SWEA 4874번 - Forth(D2)

문제 설명
- 후위 표기법으로 숫자, 연산자, '.' 을 입력받아 결과를 출력
'''

def calculate(data):
    if data == '+':
        pass

T = int(input())
for case in range(T):
    lst = input().split()

    my_list = []
    for data in lst:
        if data in '+-/*':
            try:
                my_list.append(my_list.pop() + my_list.pop())
            except IndexError:
                result = 'error'
                break
        elif data == '.':
            break
        else:
            my_list.append(int(data))
    if my_list.count != 1:
        result = 'error'
    else:
        result = my_list.pop()
    print(f'#{case+1} {result}')