"""
SWEA_4873 - 반복문자 지우기 - D2

문제
- 문자열 s에서 반복된 문자를 지우고 앞뒤를 연결하고 다시 반복문자를 확인한다.

출력
- 반복 문자를 지운 후 남은 문자열의 길이
- 남은 문자열이 없으면 0

풀이
- Stack에 넣고 같은 문자가 들어오면 pop
"""

T = int(input())
for case in range(T):
    word = input()

    top = -1
    my_stack = [0] * len(word)

    for w in word:
        if top == -1:
            top += 1
            my_stack[top] = w
        elif w == my_stack[top]:
            top -= 1
        else:
            top += 1
            my_stack[top] = w
    print(f'#{case+1} {top + 1}')
    pass

T = int(input())
for tc in range(1, T+1):
    arr = input()
    top = -1
    stack = [0] * len(arr)
    ans = 1
    # print(tc, arr)
    for i in stack:
        if i == ['(', '{', '[', '<']:
            top += 1
            stack[top] = i
        elif i == [')', '}', ']', '>']:
            if top == -1:
                ans = 0
                break
            else:
                if stack[top] == '(' and stack[i] == ')':
                    top -= 1
                elif stack[top] == '{' and stack[i] == '}':
                    top -= 1
                elif stack[top] == '[' and stack[i] == ']':
                    top -= 1
                elif stack[top] == '<' and stack[i] == '>':
                    top -= 1
    if top != -1:
        ans = 0
    print(f'#{tc} {ans}')