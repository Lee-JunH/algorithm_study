"""
SWEA_4866 - 괄호검사 - D2

문제
- 괄호가 제대로 짝을 이뤘는지 검사하는 문제

출력
- 정상적으로 짝을 이룬 경우 1
- 그렇지 않은면 0

풀이
- 스택에 여는 괄호를 넣고 다는 괄호일 때 pop을 통해 짝을 검사한다.
"""

par = {'[': ']', '{': '}', '(': ')'}

T = int(input())
for case in range(T):
    paren_str = input()

    top = -1
    stack = [0] * len(paren_str)

    ans = 1
    for x in paren_str:
        if x in ['(', '{', '[']:
            top += 1
            stack[top] = x
        elif x in [')', '}', ']']:
            if top == -1:
                ans = 0
                break
            else:
                top -= 1
                y = stack[top+1]
                if par[y] != x:
                    ans = 0
                    break
    if top != -1:
        ans = 0
    
    print(f'#{case+1} {ans}')
