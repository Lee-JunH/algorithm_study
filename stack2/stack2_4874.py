'''
SWEA 4874번 - Forth(D2)

문제 설명
- 후위 표기법으로 숫자, 연산자, '.' 을 입력받아 결과를 출력
'''

def calculate(my_list, data):
    try:
        temp1 = my_list.pop()
        temp2 = my_list.pop()
    except IndexError:
        return 'error'
    else:
        if data == '+':
            return temp2 + temp1
        elif data == '-':
            return temp2 - temp1
        elif data == '*':
            return temp2 * temp1
        elif data == '/':
            return temp2 / temp1
        

T = int(input())
for case in range(T):
    lst = input().split()

    my_list = []
    for data in lst:
        if data in '+-/*':
            result = calculate(my_list, data)
            if result == 'error':
                break
            else:
                my_list.append(result)
        elif data == '.':
            break
        else:
            my_list.append(int(data))
    if len(my_list) == 1:
        result = my_list.pop()
    else:
        result = 'error'
    print(f'#{case+1} {result}')