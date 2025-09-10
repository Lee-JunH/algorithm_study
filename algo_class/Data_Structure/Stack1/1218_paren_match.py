"""
SWEA_1218 - 괄호 짝짓기 - D4

문제
- 4종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열의 짝의 유효성 판단

출력
- 유효성 여부를 1 또는 0으로 표시

풀이
- 스택을 구현하여 유효성 검사하기
"""

T = 10
for case in range(T):
    l = int(input())
    paren = input()

    check = {'(': ')', '[': ']', '{': '}', '<': '>'}
    my_stack = []
    ans = 1
    for p in paren:
        if p in ['(', '{', '[', '<']:
            my_stack.append(p)
        else:
            if len(my_stack) == 0:
                ans = 0
                break
            temp = my_stack.pop()
            if check[temp] != p:
                ans = 0
                break
    if len(my_stack) != 0:
        ans = 0
    print(f'#{case+1} {ans}')
