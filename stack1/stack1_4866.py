# swea - 괄호검사 - D2

T = int(input())

for case in range(T):
    code = input()

    lst = []
    for s in code:
        if s == '(' or s == '{':
            lst.append(s)