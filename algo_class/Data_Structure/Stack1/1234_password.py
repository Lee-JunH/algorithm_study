"""
SWEA_1234 - 비밀번호 - D3

문제
- 0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만든다.

출력
- 비밀번호 출력
"""

def my_push(n, stack, top):
    top += 1
    stack[top] = n
    return top

T = 10
for case in range(T):
    N, password = input().split()

    top = -1
    my_stack = [0] * len(password)
    for num in password:
        if top == -1:
            top = my_push(num, my_stack, top)
        else:
            if num == my_stack[top]:
                top -= 1
            else:
                top = my_push(num, my_stack, top)
    print(f'#{case+1}', end=' ')
    for i in range(top + 1):
        print(my_stack[i], end='')
    print()

