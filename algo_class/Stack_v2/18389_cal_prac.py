"""
SWEA_18389 - 후위 유사 표기법 연습 - D1

문제
- 수식문자열을 읽어서 피연산자는 바로 출력하고
- 연산자는 스택에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오
"""

T = int(input())
for case in range(T):
    cal_str = input().strip()

    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}   #스택 밖
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}   #스택 안

    top = -1
    postfix = ''
    my_stack = [0] * len(cal_str)
    for token in cal_str:
        if token not in '(+-/*)':   
            postfix += token
        elif token == ')':
            while top > -1 and my_stack[top] != '(':
                top -= 1
                tmp = my_stack[top+1]
                postfix += tmp
            if top != -1:
                top -= 1
        else:
            if top == -1 or isp[my_stack[top]] < icp[token]:    # 아무것도 없거나 우선순위가 높으면 push
                top += 1
                my_stack[top] = token
            elif isp[my_stack[top]] >= icp[token]:
                while top > -1 and isp[my_stack[top]] >= icp[token]:
                    postfix += my_stack[top]
                    top -= 1
                top += 1
                my_stack[top] = token
    while top != -1:
        postfix += my_stack[top]
        top -= 1
    print(f'#{case+1} {postfix}')