"""
SWEA_5185 - 이진수 - D2

문제
- 16진수 1자리는 2진수 4자리로 표시된다.
- N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하라.
- 단, 2진수 앞자리 0도 반드시 출력
"""

def change(n):
    hex_lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for bin in range(16):
            if hex_lst[bin] == n:
                break
    my_stack = []
    while len(my_stack) != 4:
        my_stack.append(bin%2)
        bin //= 2
    for _ in range(4):
        print(my_stack.pop(), end='')

T = int(input())
for case in range(T):
    N, hexa = input().split()
    N = int(N)

    print(f'#{case+1} ', end='')
    for i in range(len(hexa)):
        change(hexa[i])
    print()